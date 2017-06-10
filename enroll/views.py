from django.shortcuts import render
from django.http import HttpResponse
from django.core.validators import validate_email, ValidationError
from .models import Acmer
# Create your views here.
def index(request):
    return render(request, 'enroll/index.html')
def accept(request):
    if len(request.POST['name'])== 0 or len(request.POST['name']) > 10:
        return HttpResponse('你的名字是不是太长了？')
    if len(request.POST['phone']) != 11:
        return HttpResponse('手机号必须是11位')
    try:
        validate_email(request.POST['email'])
    except ValidationError:
        return HttpResponse('邮箱不合法')
    if len(request.POST['stuno']) != 8:
        return HttpResponse('学号必须是8位')
    new_acmer = Acmer(name = request.POST['name'], phone = int(request.POST['phone']), email = request.POST['email'], stuno = request.POST['stuno'])
    new_acmer.save()
    return HttpResponse('Accepted!')
def output(request):
    Acmform = Acmer.objects.all()
    return render(request, 'enroll/output.html', {'Acmform': Acmform})
