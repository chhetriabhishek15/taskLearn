from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.


def home(request):

    return render(request, "home/homepage.html", context={"page": "HomePage"})


def signIn(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        import pdb; pdb.set_trace()
        if not User.objects.filter(username=email).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/signin/')
        
        user=authenticate(username=use)
        
    return render(request, "home/signin.html", context={"page": "SignIn"})


def signUp(request):
    if request.method == "POST":
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        User.objects.create_user(username=email,email=email, password=password,first_name=first_name,last_name=last_name)
        return redirect("/")
    return render(request, "home/signup.html", context={"page": "Signup"})
