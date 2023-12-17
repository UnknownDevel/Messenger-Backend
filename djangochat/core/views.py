from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUp

def page(request):
    return render(request, "core/frontpage.html")

def signup(request):
    if request.method == "POST":
        form = SignUp(request.POST)
        print(form.errors)
        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('page')
    else:
        form = SignUp()
    
    return render(request, "core/signup.html", {"form": form})

# Create your views here.
