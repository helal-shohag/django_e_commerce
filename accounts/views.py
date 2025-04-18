from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import authenticate,login,logout
from django.utils.http import urlsafe_base64_decode
from django.contrib import messages
from .models import CustomUser
from .forms import CustomUserForm



# Create your views here.
def home(request):
    return render(request,'home.html') 


def user_register(request):    
    if request.method == "POST":
       form = CustomUserForm(request.POST)
       if form.is_valid():
          user = form.save()
          # login(request,user)
          return redirect("login")
    else:
        form = CustomUserForm()  

    return render(request,'accounts/signup.html')
       
def user_login(request): 
    if request.method == "POST":
       email = request.POST.get("email")
       password = request.POST.get("password")
       user = authenticate(request,email = email,password = password)
       if not user:
          messages.error(request,'Invalid Username or password')
       else:
          login(request,user)
          messages.success(request,'You have successfully Logged in')
          return redirect("profile")   
    
    return render(request,'accounts/login.html')

@login_required
def user_logout(request):
   logout(request)
   return redirect('signup')

def user_dashboard(request):
   return render(request,'accounts/profile.html')