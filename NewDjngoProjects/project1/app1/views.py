from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.


def welcome(request):
    response = HttpResponse()
    response.write("<h2>Welcome to Django</h2>")
    return response


def login(request):
    dt = datetime.datetime.now()
    output = f'''<html>
    <body bgcolor=cyan>
    <h2>The current Date and Time of login is {dt}</h2>
    <h2>This is login Page</h2>
    </body></html>'''
    response = HttpResponse()
    response.write(output)
    return response
    
def logout(request):
    dt=datetime.datetime.now()
    output=f'''<html>
    <body bgcolor=yellow>
    <h2>The current date and time for logout is {dt}</h2>
    <h2>This is logout page</h2>
    </body></html>'''
    response = HttpResponse()
    response.write(output)
    return response

def first(request):
    response=render(request,'welcome.html',context={})
    return response

def add1(request):
    n1 = 10
    n2 = 20
    n3 = n1 + n2
    response=render(request,"add_res.html",context={'n1':n1,'n2':n2,'n3':n3})
    return response


def add(request,n1,n2):
    n3=n1+n2
    response=render(request,"result.html",context={'n1':n1,'n2':n2,'n3':n3})
    return response