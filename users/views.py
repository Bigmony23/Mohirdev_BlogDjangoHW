from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from django.views import View

from users.forms import UserCreationForm


class RegisterView(View):
    def get(self, request):
        register_form=UserCreationForm()
        context = {'register_form': register_form}
        return render(request, 'register.html',context)
    def post(self, request):
        register_form=UserCreationForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            return redirect('login')
        else:
            context = {'register_form': register_form}
            return render(request, 'register.html',context)
class LoginView(View):
    def get(self, request):
        login_form=AuthenticationForm()
        context = {'login_form': login_form}
        return render(request, 'login.html',context)
    def post(self, request):
        login_form=AuthenticationForm(request,data=request.POST)
        if login_form.is_valid():
            user=login_form.get_user()
            login(request,user)
            messages.success(request,'You are now logged in')
            return redirect('home')
        else:
           return render(request,'login.html',{'login_form':login_form})
class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.info(request,'You are now logged out')
        return redirect('home')


# Create your views here.
