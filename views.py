from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm

# View to handle form submission and set session data
def set_session(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # Accessing cleaned data
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            # Setting session data
            request.session['username'] = username
            request.session['email'] = email 
            return redirect('get_session')
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'form': form})

# View to retrieve and display session data
def get_session(request):
    username = request.session.get('username', 'Guest')
    email = request.session.get('email', 'Not Provided')
    return render(request, 'session_display.html', {'username': username, 'email': email})

# View to handle form submission and set cookie data
def set_cookie(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # Accessing cleaned data
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            # Setting cookie data
            response = redirect('get_cookie')
            response.set_cookie('username', username, max_age=3600)
            response.set_cookie('email', email, max_age=3600)
            return response
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'form': form})

# View to retrieve and display cookie data
def get_cookie(request):
    username = request.COOKIES.get('username', 'Guest')
    email = request.COOKIES.get('email', 'Not Provided')
    return render(request, 'cookie_display.html', {'username': username, 'email': email})
