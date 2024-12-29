from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from accounts.models import Post

# Create your views here.


def home_page(request):
    posts = None

    if request.user.is_authenticated:
        posts = Post.objects.all()

    return render(request, "blogpage/index.html", context={"posts": posts})


@login_required(login_url="/login-page/")
def post_page(request):
    if request.method == "POST":
        post_title = request.POST.get("post_title")
        post_body = request.POST.get("post_body")

        post = Post.objects.create(
            user=request.user, post_title=post_title, post_body=post_body
        )
        post.save()

        return redirect("/")
    return render(request, "blogpage/post.html")


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not User.objects.filter(username=username).exists():
            messages.info(request, "Username dosen't exists")
            return redirect("/register-page/")

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, "Invalid Password")
        else:
            login(request, user)
            return redirect("/")

    return render(request, "authentication/login_page.html")


def logout_page(request):
    logout(request)
    return redirect("/login-page/")


def register(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.info(request, "Username taken")
            return redirect("/register-page/")

        user = User.objects.create(first_name=full_name, username=username)
        user.set_password(password)

        success = user.save()
        messages.success(request, "Registered Successfully")

    return render(request, "authentication/register.html")
