from django.shortcuts import render

# Create your views here.
def login_view(request):
    template_view = "auth-login.html"
    return render (request,template_name=template_view)

# View for register
def register_view(request):
    template_view = "auth-register.html"
    return render (request,template_name=template_view)

# View for forget
def forgot_view(request):
    template_view = "auth-forgot-password.html"
    return render (request,template_name=template_view)