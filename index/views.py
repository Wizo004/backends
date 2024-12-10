from django.shortcuts import render, redirect
from .forms import CustomLoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index/index.html')


def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Replace 'home' with the name of the page to redirect after login
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = CustomLoginForm()

    return render(request, 'registration/login.html', {'form': form})


# This view is optional, but it's good to protect any page you want only logged-in users to access.
@login_required
def home_view(request):
    return render(request, 'index/index.html')





# Create your views here.
