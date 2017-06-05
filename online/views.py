# -*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
from online.models import User
from PIL import Image, ImageFont, ImageDraw
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
from random import randint
from django.shortcuts import render

class UserForm(forms.Form): 
    username = forms.CharField(label='username',max_length=100)
    password = forms.CharField(label='password',widget=forms.PasswordInput())


def regist(req):
    if req.method == 'POST':
        if(check(req)):
            uf = UserForm(req.POST)
            if uf.is_valid():
                # 下两行是不是可以更改？
                username = uf.cleaned_data['username']
                password = uf.cleaned_data['password']
                if (User.objects.filter(username__exact=username)):
                    return HttpResponse('该用户名已存在！')
                else:
                    User.objects.create(username= username,password=password)
                    return HttpResponse('注册成功!')
        else:
            return HttpResponse('验证码输入错误，请重新输入')
    else:
        uf = UserForm()
    # return render_to_response('online/regist.html',{'uf':uf})
    return render(req, 'online/regist.html', {'uf':uf})


def login(req):
    if req.method == 'POST':
        if (check(req)):
            uf = UserForm(req.POST)
            if uf.is_valid():
                username = uf.cleaned_data['username']
                password = uf.cleaned_data['password']
                user = User.objects.filter(username__exact = username,password__exact = password)
                if user:
                    response = HttpResponseRedirect('/online/index/')
                    # response.set_cookie('username',username,3600)
                    req.session['username'] = username;
                    return response
                else:
                    if(User.objects.filter(username__exact = username)):
                        return HttpResponse('密码错误！请重新输入。')
                    else:
                        return HttpResponse('不存在的用户名！')
                    # return HttpResponseRedirect('/online/login/')
        else:
            return HttpResponse('验证码输入错误，请重新输入')
    else:
        uf = UserForm()
    # return render_to_response('login.html',{'uf':uf})
    return render(req, 'online/login.html', {'uf':uf})


def index(req):
    # username = req.COOKIES.get('username','')
    username = req.session.get('username', '')
    # return render_to_response('index.html' ,{'username':username})
    return render(req, 'online/index.html', {'username':username})


def logout(req):
    response = HttpResponse('logout !!')
    # response.delete_cookie('username')
    try:
        del req.session['username']
    except KeyError:
        pass
    return response


# 进入验证码界面接口(temp.html)
def temp(request):
    return render(request,'online/temp.html')

# 功能接口：返回验证码输入正确与否（忽略大小写），并返回一个布尔值(0-输入错误，1-输入正确)
def check(request):
    flag = 0
    if request.POST['verify'].lower() == request.session['verify'].lower():
        flag = 1
        return flag
    else:
        return flag

 # 功能接口：返回验证码图片
def verify(request, width, height):
    wordsCount = 4# 验证码字符长度
    width = int(width)# 图片宽度
    height = int(height)# 图像高度
    size = int(min(width / wordsCount, height) / 1.3)# 字体大小设置
    bgColor = (randint(200, 255), randint(200, 255), randint(200, 255))# 随机背景色
    img = Image.new('RGB', (width, height), bgColor)# 创建图像
    font = ImageFont.truetype('arial.ttf', size)# 导入字体
    draw = ImageDraw.Draw(img)# 创建画笔
    text = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    verifytext = ''
    for i in range(wordsCount):
        textColor = (randint(0, 160), randint(0, 160), randint(0, 160))
        left = width * i / wordsCount + (width / 4 - size) / 2
        top = (height - size) / 2
        word = text[randint(0, len(text) - 1)]
        verifytext += word
        draw.text((left, top), word, font=font, fill=textColor)
    for i in range(30):
        textColor = (255, 255, 255)
        left = randint(0, width)
        top = randint(0, height)
        draw.text((left, top), '*', font=font, fill=textColor)
     # 画线条
    for i in range(5):
        linecolor = (randint(0, 160), randint(0, 160), randint(0, 160))
        line = (randint(0, width), randint(0, height), randint(0, width), randint(0, height))
        draw.line(line, fill=linecolor)
    del draw
    mstream = StringIO()
    img.save(mstream, 'jpeg')
    request.session['verify'] = verifytext
    return HttpResponse(mstream.getvalue(), 'image/jpeg')