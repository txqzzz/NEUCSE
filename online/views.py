# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from online.models import UserProfile
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render
from django.conf import settings
from django.core.urlresolvers import reverse
from geetest import GeetestLib
from django.utils import timezone
from .models import create_user_profile
from django.db.models.signals import post_save



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
                if (User.objects.filter (username__exact=username)):
                    return HttpResponse('该用户名已存在！')
                else:
                    user = User.objects.create_user(username,"",password)
                    user.save()
                    user.date_joined=timezone.now()
                    post_save.connect(create_user_profile, sender=User)
                    # return HttpResponse('注册成功!')  提示框
                    return render(req, 'online/login.html', {'uf': uf})
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
                # authenticate() 验证给出的username和password是否是一个有效用户。如果有效，则返回一个User对象，无效则返回None。
                user = auth.authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        user.last_login = timezone.now()
                        auth.login(req, user)
                        response = HttpResponseRedirect(reverse('online:index'))
                        req.session['username'] = username
                        return response
                    else:
                        return HttpResponse('锁定状态无法使用')
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
        auth.logout(req)
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



# fuck check  permission
# if request.user.is_authenticated():
#     针对已经登录验证的用户
# else:
#     对匿名用户