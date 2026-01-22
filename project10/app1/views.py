from django.shortcuts import render
from  app1.models import UserRegister
from django.http import HttpResponse 
# Create your views here.


def register_view(request):
    name=request.GET.get('name')
    uname=request.GET.get('uname')
    pwd=request.GET.get("pwd")
    user=UserRegister(name=name,uname=uname,password=pwd)
    user.save()
    response=HttpResponse("user Registered")
    return response

def home(request):
    response = render(request,"user_register.html",context={})
    return response 