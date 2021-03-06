from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.validators import validate_email, ValidationError
from .models import Acmer, Lecture
from django.conf.urls.static import static
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
    new_acmer = Acmer(name=request.POST['name'], phone=request.POST['phone'], email = request.POST['email'], stuno = request.POST['stuno'],
                      major=request.POST['major'])

    new_acmer.save()
    return render(request, 'enroll/index.html', {'ok': 1})


def output(request):

    Acmform = Acmer.objects.all()
    Acmform = {i.stuno: i for i in Acmform}
    return render(request, 'enroll/output.html', {'Acmform': Acmform.values})
