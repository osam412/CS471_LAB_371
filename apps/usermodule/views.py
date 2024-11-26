from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth.forms import UserCreationForm # type: ignore
from django.contrib import messages # type: ignore
from django.contrib.auth import authenticate, login # type: ignore
from django.contrib.auth.forms import AuthenticationForm # type: ignore
from django.contrib.auth import logout  # type: ignore

def registerUser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully registered.')
            return redirect('login')
        else:
            messages.error(request, 'Registration failed. Please correct the error.')
    else:
        form = UserCreationForm()
    return render(request, 'usermodule/register.html', {'form': form})



def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('listBooks_part1')  # Redirect to any page you want
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid login credentials.')
    else:
        form = AuthenticationForm()
    return render(request, 'usermodule/login.html', {'form': form})

def logoutUser(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('login')  # Redirect to the homepage or any landing page



