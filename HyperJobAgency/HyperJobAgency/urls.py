"""HyperJobAgency URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from agency.views import MenuPage, SignupPage, LoginPage, HomePage
from resume.views import ResumesPage
from vacancy.views import VacanciesPage


urlpatterns = [
    path('', MenuPage.as_view()),
    path('home/', HomePage.as_view()),
    path('signup/', SignupPage.as_view()),
    path('login/', LoginPage.as_view()),
    path('resumes/', ResumesPage.as_view()),
    path('vacancies/', VacanciesPage.as_view()),
    path('admin/', admin.site.urls),
]
