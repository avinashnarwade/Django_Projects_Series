from django.shortcuts import render,redirect
from .models import Student


# Create your views here.


def student_form(request):
    if request.method =="POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        college_id = request.POST.get('college_id')
        address = request.POST.get('address')
        
        
        Student.objects.create(
            first_name = first_name,
            last_name = last_name,
            college_id = college_id,
            address = address
            
        )
        return redirect('/success/')
    return render(request,'student_form.html')

def success(request):
    return render(request,'success.html')