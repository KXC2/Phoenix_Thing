from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import PhoenixForms
from .models import Puns, Thoughts, DiaryEntry

# Create your views here.

def user_login(request):
    """
    Renders the index page upon user login request.

    This view is typically accessed after a successful login or
    directly via URL. It does not process any input.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: The rendered 'index.html' page.
    """
    return render(request, 'index.html')


def authenticate_user(request):
    """
    Authenticates a user using POSTed username and password.

    If the authentication is successful, the user is logged in and
    redirected to the home page. Otherwise, they are redirected back
    to the login page.

    Args:
        request (HttpRequest): The HTTP request containing POST data.

    Returns:
        HttpResponse: Redirect to 'home.html' or back to login page.
    """
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is None:
        return redirect('Personal:login')
    else:
        login(request, user)
        return render(request, 'home.html')


def account_creation(request):
    """
    Handles user account creation using the PhoenixForms form.

    If the request method is POST and the form is valid, a new account
    is created and the user is redirected to the home page with a success message.
    Otherwise, the registration form is displayed again.

    Args:
        request (HttpRequest): The HTTP request containing form data.

    Returns:
        HttpResponse: The rendered registration or home page.
    """
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
    """
    Displays the five most recent diary entries.

    Fetches the latest diary entries (ordered by publication date)
    and renders them to the 'PhoenixDiary.html' template.

    Args:
        request (HttpRequest): The HTTP request.

    Returns:
        HttpResponse: The rendered 'PhoenixDiary.html' with diary entries.
    """
    Latest_diary = DiaryEntry.objects.order_by('-pub_date')[:5]
    return render(request, "PhoenixDiary.html", {
        'Latest_diary': Latest_diary,
    })


def jokes(request):
    """
    Displays all pun entries.

    Fetches all puns from the database and renders them to the 'puns.html' template.

    Args:
        request (HttpRequest): The HTTP request.

    Returns:
        HttpResponse: The rendered 'puns.html' with pun content.
    """
    Latest_pun = Puns.objects.all()
    return render(request, "puns.html", {
        'Latest_pun': Latest_pun,
    })


def thoughts(request):
    """
    Displays the five most recent thoughts.

    Fetches the latest thoughts (ordered by publication date)
    and renders them to the 'thoughts.html' template.

    Args:
        request (HttpRequest): The HTTP request.

    Returns:
        HttpResponse: The rendered 'thoughts.html' with thought entries.
    """
    Latest_thoughts = Thoughts.objects.order_by('-pub_date')[:5]
    return render(request, "thoughts.html", {
        'Latest_thoughts': Latest_thoughts,
    })
