from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            context = {'error': 'Invalid username or password'}
            return render(request, 'accounts/login.html', context)
        login(request, user)
        return redirect('/')
    return render (request, 'accounts/login.html', {})