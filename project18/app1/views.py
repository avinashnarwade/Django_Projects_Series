from django.shortcuts import render
from django.http import HttpResponse 
from app1.forms import PersonForm
# Create your views here.

def personview(request):
    if request.method=="POST":
        form=PersonForm(request.POST)
        if form.is_valid():
            return HttpResponse("<h2>Valid Data</h2>")
        else:
            form=PersonForm()
    response =render(request,"person_temp.html",context = {'form:form'})
    return response 



