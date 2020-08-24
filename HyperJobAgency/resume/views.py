from django.shortcuts import render, redirect
from django.views import View
from resume.models import Resume

# Create your views here.


class ResumesPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'resume/resumes_page.html', {'resumes': Resume.objects.all()})
