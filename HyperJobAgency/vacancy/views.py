from django.shortcuts import render, redirect
from django.views import View
from vacancy.models import Vacancy

# Create your views here.


class VacanciesPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'vacancy/vacancies_page.html', {'vacancies': Vacancy.objects.all()})
