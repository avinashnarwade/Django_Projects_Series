from django.shortcuts import render

# Create your views here.


def add_view(request):
    num1=eval(request.GET.get('n1'))
    num2=eval(request.GET.get('n2'))
    num3=num1+num2
    response=render(request,'result.html',context={'num1':num1,'num2':num2,'num3':num3})
    return response


def home(request):
    response=render(request,'calc.html',context={})
    return response
