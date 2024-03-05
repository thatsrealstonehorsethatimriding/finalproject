from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        User.objects.create_user(username=username, email=email, password=password)
        return redirect('login')
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        authenticate(request)
        return redirect('dashboard')  
    else:
        return render(request, 'login.html')

    
def authenticate(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.get(username=username)
        if user.check_password(password):
            return redirect('dashboard')
        else:
            return redirect('login')
    return render(request, 'login.html')


def dashboard(request):
    return render(request, 'dashboard.html')


