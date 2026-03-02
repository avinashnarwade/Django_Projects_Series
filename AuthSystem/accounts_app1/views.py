from django.shortcuts import render,redirect
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm
)

# Create your views here.


from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required

def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request,user)
        return redirect('dashboard')
    return render(request,'accounts/register.html',context={'form':form})

def login_view(request):
    form = AuthenticationForm(request,data=request.POST or None)
    if form.is_valid():
        user = form.get_user()
        login(request,user)
        return redirect('dashboard')
    return render(request,'accounts/login.html',context={'form':form})
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def change_password(request):
    form = PasswordChangeForm(request.user,request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request,'accounts/change_password.html',context={'form':form})

def reset_password(request):
    form = PasswordResetForm(request.POST or None)
    if form.is_valid():
        form.save(request=request)
        return redirect('login')
    return render(request,'accounts/reset_password.html',{'form':form})
    