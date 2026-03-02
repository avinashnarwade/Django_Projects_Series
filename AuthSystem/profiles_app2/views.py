from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required


@login_required 
def profile_view(request):
    return render(request,'profile/profile.html')


@login_required
def edit_profile(request):
    form = UserChangeForm(request.POST or None, instance=request.user)
    if form.is_valid():
        form.save()
        return redirect('profile')

    return render(request,'profile/edit_profile.html',context={'form':form})


# Create your views here.
