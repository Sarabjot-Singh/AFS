from django.shortcuts import render, redirect
from .forms import (
    UserRegisterForm,
    ProfileRegistrationForm,
    UserUpdateForm,
    ProfileUpdateForm,
    RechargeForm)

from django.contrib import messages
from users.models import Profile
from users.qrcodegenerator import qrcode

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        profile_form = ProfileRegistrationForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit = False)
            profile.user = user
            profile.save()
            username = form.cleaned_data.get('username')
            mobile = str(profile_form.cleaned_data.get('mobile'))
            data = username + str(mobile)
            qrcode(username, mobile)
            Profile.objects.filter(mobile=mobile).update(qr_code=f'qr_codes/{data}.png')
            messages.success(request, f"Account created for {username} Now you can login using account credentials")
            return redirect('login')
    else:
        form = UserRegisterForm()
        profile_form = ProfileRegistrationForm()
    return render(request, template_name='users/register.html', context={'form':form, 'profile_form':profile_form})

def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile
                                   )

        if p_form.is_valid() and u_form.is_valid():
            u_form.save()
            p_form.save()
            username = u_form.cleaned_data.get('username')
            mobile = p_form.cleaned_data.get('mobile')
            data = username + str(mobile)
            Profile.objects.filter(mobile=mobile).first().qr_code.delete(save=True)
            qrcode(username, mobile)
            Profile.objects.filter(mobile=mobile).update(qr_code=f'qr_codes/{data}.png')
            return redirect('scago-home')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request, 'users/profile.html', context)

def recharge(request):
    if request.method == 'POST':
        r_form = RechargeForm(request.POST, instance=request.user.profile)
        if r_form.is_valid():
            mobile = request.user.profile.mobile
            balance = r_form.cleaned_data.get('balance')

            Profile.objects.filter(mobile=mobile).update(balance=balance)
            return redirect('recharge')

    else:
        r_form = RechargeForm(instance=request.user.profile)

    context = {
        'r_form':r_form
    }
    return render(request, 'users/recharge.html', context)
