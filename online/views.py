# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from online.models import User
from django.shortcuts import render
from django.conf import settings
from django.core.urlresolvers import reverse
from geetest import GeetestLib


class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())


def regist(req):
    if req.method == 'POST':
        if (geetest_post_validate(req)):
            uf = UserForm(req.POST)
            if uf.is_valid():
                username = uf.cleaned_data['username']
                password = uf.cleaned_data['password']
                if (User.objects.filter(username__exact=username)):
                    return HttpResponse('该用户名已存在！')
                else:
                    User.objects.create(username=username, password=password)
                    return HttpResponse('注册成功!')
        else:
            return HttpResponse('验证码输入错误，请重新输入')
    else:
        if req.session.get('username', False):
            return HttpResponseRedirect(reverse('online:index'))
        else:
            uf = UserForm()
            return render(req, 'online/regist.html', {'uf': uf})


def login(req):
    if req.method == 'POST':
        if (geetest_post_validate(req)):
            uf = UserForm(req.POST)
            if uf.is_valid():
                username = uf.cleaned_data['username']
                password = uf.cleaned_data['password']
                user = User.objects.filter(username__exact=username, password__exact=password)
                if user:
                    response = HttpResponseRedirect(reverse('online:index'))
                    req.session['username'] = username
                    return response
                else:
                    return HttpResponse('用户名或密码不正确')
        else:
            return HttpResponse('验证码输入错误，请重新输入')
    else:
        if req.session.get('username', False):
            return HttpResponseRedirect(reverse('online:index'))
        else:
            uf = UserForm()
            return render(req, 'online/login.html', {'uf': uf})


def index(req):
    username = req.session.get('username', '')
    return render(req, 'online/index.html', {'username': username})


def logout(req):
    try:
        del req.session['username']
    except KeyError:
        pass
    return HttpResponseRedirect(reverse('online:login'))


# 极验初始化后端函数
def geetest_get_captcha(request):
    gt = GeetestLib(settings.GEETEST_ID, settings.GEETEST_KEY)
    status = gt.pre_process()
    request.session[gt.GT_STATUS_SESSION_KEY] = status
    response_str = gt.get_response_str()
    return HttpResponse(response_str)


# 极验二次验证函数，成功返回True，失败返回False
def geetest_post_validate(request):
    gt = GeetestLib(settings.GEETEST_ID, settings.GEETEST_KEY)
    challenge = request.POST.get(gt.FN_CHALLENGE, '')
    validate = request.POST.get(gt.FN_VALIDATE, '')
    seccode = request.POST.get(gt.FN_SECCODE, '')
    status = request.session[gt.GT_STATUS_SESSION_KEY]
    if status:
        result = gt.success_validate(challenge, validate, seccode)
    else:
        result = gt.failback_validate(challenge, validate, seccode)
    return result
