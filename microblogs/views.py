from django.shortcuts import render, redirect
from microblogs.models import User
from microblogs.forms import LogInForm, SignUpForm

def home(request):
    return render(request, "home.html")

def feed(request):
    return render(request, "feed.html")

def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("feed")
    else:
        form = SignUpForm()
    return render(request, "sign_up.html", {"form": form})

def log_in(request):
    form  = LogInForm()
    return render(request, "log_in.html", {"form": form})