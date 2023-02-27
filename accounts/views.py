from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login
from django.contrib import messages



# Our register view
def Register_View(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save() # save passed data
            login(request, user) # login the user
            messages.success(request, "Registration Successful")
            return redirect("/")
        messages.error(request, "Invalid information")
    return render(request, "register.html", {"register_form": form})

