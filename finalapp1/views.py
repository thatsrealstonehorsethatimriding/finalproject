from django.shortcuts import render, redirect
from .models import User

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        User.objects.create(username=username, password=password, email=email)
        return redirect('login')
    return render(request, 'register.html')
