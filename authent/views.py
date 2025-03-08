from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
def Login_(request):

    if request.method=="POST":
        user=request.POST['username']
        passw=request.POST['password']
        a=authenticate(username=user,password=passw)
        if a is not None:
            login(request,a)
            return redirect('home')
        else:
            messages.error(request, "Incorrect Username or Password.Try Again.")
            return redirect("login")
        
    return render(request,'login.html')

def Register_(request):
    if request.method == 'POST':
        user=request.POST['username']
        email=request.POST['email']
        passw=request.POST['password']
        if User.objects.filter(username=user).exists():
            messages.error(request, "Username already taken. Choose another.")
            return redirect("register")
        a=User.objects.create(username=user,email=email,password=passw)
        a.set_password(passw)
        a.save()
        
        return redirect('login')
    return render(request,'register.html')



def Logout_(request):
    logout(request)
    return redirect('login') 
# def profile(request):
#     return render(request,'profile.html')
@login_required(login_url='login')
def profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html')
    else:
        return render(request,'login.html')