from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import PhoenixForms
from .models import Puns, Thoughts, DiaryEntry

# Create your views here.

def user_login(request):

    return render(request, 'index.html')

def authenticate_user(request):

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is None:
        return redirect('Personal:login')

    
    else:
        login(request, user)
        return render(request, 'home.html')


def account_creation(request):

    if request.method == 'POST':
        form = PhoenixForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully.")
            return render(request, 'home.html')
    else:
        form = PhoenixForms()
    return render(request, 'Register.html', {'form': form})

def phoenixDiary(request):

    Latest_diary = DiaryEntry.objects.order_by('-pub_date')[:5]
    return render(request, "PhoenixDiary.html", {
    'Latest_diary': Latest_diary,
    })

def jokes(request):

    Latest_pun = Puns.objects.all()
    return render(request, "puns.html", {
    'Latest_pun': Latest_pun,
    })

def thoughts(request):

    Latest_thoughts = Thoughts.objects.order_by('-pub_date')[:5]
    return render(request, "thoughts.html", {
    'Latest_thoughts': Latest_thoughts,
    })