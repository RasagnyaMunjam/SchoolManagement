from django.contrib.auth import authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render

def home(request):
    return render(request, "home.html")

# Create your views here.
def teacherlogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            return HttpResponseRedirect('/home')
    form = AuthenticationForm
    return render(request, "login.html", {"form": form})


def teacherlogout(request):
    logout(request)
    return HttpResponseRedirect('/')
