from django.shortcuts import render,redirect
from django.template.loader import get_template

from .forms import LoginForm,SignupForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from django.conf import settings
from django.core.mail import send_mail,EmailMultiAlternatives

# Create your views here.
def LoginView(request):
    # if request.method == 'GET':
    #     if request.user.is_authenticated:
    #         return redirect('/home')
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():

            user=authenticate(username=form.cleaned_data['username'],
                              password=form.cleaned_data['password'])
            if user:
                print('user',user)
                login(request,user)
                return redirect('/home')
            else:
                print('Not authenticated')
    # elif request.method=='GET':
    #     if request.user.is_authenticated:
    #         return redirect('/home')
    form=LoginForm()
    return render(request,'accounts/login.html',{'form':form})

@transaction.atomic
def ProfileView(request):
    html_file=get_template('accounts/mailtemplate.html')
    html_content=html_file.render()
    
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(
                request,
                f'Your profile has been updated successfully'
            )
            return redirect('accounts:profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'accounts/profile.html', context)




def SignupView(request):
    if request.method=='GET':
        if request.user.is_authenticated:
            return redirect('/accounts/profile')
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            print('form is valid')
            user=User(username=form.cleaned_data['username'],
                      first_name=form.cleaned_data['first_name'],
                      last_name=form.cleaned_data['last_name'],
                      email=form.cleaned_data['email'])
            user.save()
            user.set_password(form.cleaned_data['password'])
            user.save()
            sub='Confirmation'
            from_email= settings.EMAIL_HOST_USER
            to=[settings.EMAIL_RECEIVER, ]
            msg=EmailMultiAlternatives(subject=sub, from_email=from_email, to=to )
            msg.attach_alternative(html_content,'text/html')
            msg.send()
            print('user',user)
            return redirect('/accounts/login/')
    elif request.method=='GET':
        form=SignupForm()

    return render(request,'accounts/signup.html',{'form':form})


def LogoutView(request):
    logout(request)
    return redirect('/accounts/login/')



