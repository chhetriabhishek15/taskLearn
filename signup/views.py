from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.


def home(request):

    return render(request, "home/homepage.html", context={"page": "HomePage"})


def signIn(request):
    if request.method == "POST":
        DATA = request.POST
        email = DATA.get("email_Add")
        passwd = DATA.get("passwd")

        User.objects.create_user(username=email, email=email, password=passwd)
        return redirect("/signin/")
    return render(request, "home/signin.html", context={"page": "SignIn"})


def signUp(request):
    return render(request, "home/signup.html", context={"page": "Signup"})
