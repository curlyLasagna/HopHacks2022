from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

from auth_app.forms import PersonRegistrationForm, PersonLoginForm

# Create your views here.
def register(request):
    if request.method == 'GET':
        form = PersonRegistrationForm()
        return render(request, 'register.html', {'form': form})
    else:
        form = PersonRegistrationForm(request.POST)
        if form.is_valid():
            fn = form.cleaned_data['first_name']
            ln = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            uname = form.cleaned_data['username']
            pswd = form.cleaned_data['password']

            User.objects.create_user(first_name=fn, last_name=ln, email=email,
                    username=uname, password=pswd)

              
            messages.success(request, 'user crerated successfully.')
            return redirect('login')
        else:
            return render(request, 'register.html', {'form':form})

def signin(request):
    if request.method == 'GET':
        form = PersonLoginForm()
        return render(request, 'login.html', {'form': form})
    else:
        next_url = request.GET.get('next')
        form = PersonLoginForm(request.POST)
        uname = request.POST['username']
        pswd = request.POST['password']

        user = authenticate(username=uname, password=pswd)
        if user is not None:
            login(request, user)
            if next_url is None:
                return redirect('home')
            else:
                return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password.')
            messages.error(request, 'Please try again later.')
            return render(request, 'login.html', {'form': form})


def signout(request):
    logout(request)
    return redirect('login')