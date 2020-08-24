from django.shortcuts import render, redirect

from django.views.generic.base import TemplateView
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

from django.contrib.auth.models import User
from resume.models import Resume
from vacancy.models import Vacancy
from django.http import HttpResponseForbidden

# Create your views here.


class MenuPage(TemplateView):
    template_name = 'agency/menu_page.html'


class SignupPage(CreateView):
    form_class = UserCreationForm
    success_url = '/login'
    template_name = 'agency/signup_page.html'


class LoginPage(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    template_name = 'agency/login_page.html'


class HomePage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'agency/home_page.html')
    
    def post(self, request, *args, **kwargs):
        description = request.POST.get('description')
        if request.user.is_authenticated and not request.user.is_staff:
            Resume.objects.create(description=description, author=request.user)
            return redirect('/home')
        elif request.user.is_authenticated and request.user.is_staff:
            Vacancy.objects.create(description=description, author=request.user)
            return redirect('/home')
        else:
            return HttpResponseForbidden()
