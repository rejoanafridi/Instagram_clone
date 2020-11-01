from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import get_user
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def post_details(request):
    return render(request, 'main/post_details.html')


def tag(request):
    return render(request, 'main/tag.html')


def profile(request):
    return render(request, 'main/profile.html')


def registration(request):
    if request.user.is_authenticated:
        return redirect('login_page')
    else:
        if request.method == 'GET':
            return render(request, 'main/signup.html')
        elif request.method == 'POST':
            first_name = request.POST['firstName']
            last_name = request.POST['lastName']
            username = request.POST['username']
            email = request.POST['useremail']
            password = request.POST['userPassword']

            username_count = User.objects.filter(username=username).count()
            email_count = User.objects.filter(email=email).count()

            if username_count == 0 and email_count == 0:
                User.objects.create_user(
                    username=username, email=email, password=password)
                return redirect('login_page')

            elif username_count > 0:
                return render(request, 'main/signup.html', {'msg': 'This username is in used'})

            elif email_count > 0:
                return render(request, 'main/signup.html', {'msg': 'This email is in used'})

            return render(request, 'main/signup.html')


def login(request):
    return render(request, 'main/login.html')
