from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required

from .forms import *

def loginRegisterPageView(request):    
        if request.POST:
            formRegister = registerForm(request.POST) 
            if request.POST.get("sign-up"):
                if formRegister.is_valid():
                    register = formRegister.save()
                    user_group = Group.objects.get(name="Client")
                    register.groups.add(user_group)
                    messages.info(request, 'Vous avez creer votre compte, go to login  ')
                    
            if request.POST.get("sign-in"):
                username1 = request.POST['username']
                password1 = request.POST['password1']
                user = authenticate(request, username=username1, password=password1)
                
                if user is not None:
                    login(request, user)
                    messages.info(request, 'Vous ete connecter  ')
                return redirect('home')


        else:
            formRegister = registerForm()
        context = {'formRegister' : formRegister}
        return render(request, 'front/Login-register.html', context )


def logoutview(request):
    logout(request)
    return redirect('home')
            