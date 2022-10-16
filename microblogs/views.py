from django.shortcuts import render, redirect
from microblogs.models import User, Post
from microblogs.forms import LogInForm, PostForm, SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    return render(request, "home.html")

def feed(request):
    form = PostForm()
    return render(request, "feed.html", {"form": form})

def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("feed")
    else:
        form = SignUpForm()
    return render(request, "sign_up.html", {"form": form})

def log_in(request):
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("feed")
        messages.add_message(request, messages.ERROR, "The credentials provided were invalid!")
    form  = LogInForm()
    return render(request, "log_in.html", {"form": form})

def log_out(request):
    logout(request)
    return redirect("home")

def user_list(request):
    users = User.objects.all()
    return render(request, "user_list.html", {"users": users})

def show_user(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, "show_user.html", {"user": user})

def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if request.user and form.is_valid():
            post = form.save(commit=False) 
            post.author = request.user
            post.save()

        return redirect("feed")