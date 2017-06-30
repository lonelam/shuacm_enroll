from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.validators import validate_email, ValidationError
from django.db import IntegrityError
from .models import Acmer, Lecture
# Create your views here.


def index(request):
    lectable = Lecture.objects.all()
    return render(request, 'enroll/index.html', {'lectable':lectable, 'ok': -1})


def accept(request):
    if len(request.POST['name']) == 0 or len(request.POST['name']) > 10:
        return render(request, 'enroll/index.html', {'ok': 2, 'msg':'你的名字是不是太长了？'})
    if len(request.POST['phone']) != 11:
        return render(request, 'enroll/index.html', {'ok': 2, 'msg':'手机号必须是11位'})
    try:
        validate_email(request.POST['email'])
    except ValidationError:
        return render(request, 'enroll/index.html', {'ok': 2, 'msg':'邮箱不合法'})
    if len(request.POST['stuno']) > 10:
        return render(request, 'enroll/index.html', {'ok': 2, 'msg':'您学号是不是太长了？'})
    try:
        new_acmer = Acmer(name=request.POST['name'], phone=request.POST['phone'], email=request.POST['email'],
                          stuno=request.POST['stuno'],
                          major=request.POST['major'])
        #Acmer.objects.get(stuno=request.POST['stuno'])
        new_acmer.save()
    except IntegrityError:
        return render(request, 'enroll/index.html', {'ok': 2, 'msg': '学号或手机已存在'})
    return render(request, 'enroll/index.html', {'ok': 1})


def output(request):
    Acmform = Acmer.objects.all()
    Acmform = {i.stuno: i for i in Acmform}
    return render(request, 'enroll/output.html', {'Acmform': Acmform.values})
