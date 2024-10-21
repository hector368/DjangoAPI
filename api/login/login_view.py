from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages


# Create your views here.
def login_view(request):
    template_name= "auth-login.html"
    
        # Validación para usuarios ya autenticados
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid login Credentials')
    return render (request,template_name)

# View for register
def register_view(request):
    template_name= "auth-register.html"
    return render (request,template_name)

# View for forget
def forgot_view(request):
    template_name= "auth-forgot-password.html"
    return render (request,template_name)

#View for logout
def logout_view(request):
    logout(request)
    return redirect('login')