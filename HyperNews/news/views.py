from django.shortcuts import render, redirect
from django.conf import settings

from django.http import Http404
from django.views import View

import json
import datetime


with open(settings.NEWS_JSON_PATH, 'r') as data_file:
    data = json.load(data_file)


class StartPage(View):
    def get(self, request, *args, **kwargs):
        return redirect('/news')


class NewsPage(View):
    def get(self, request, *args, **kwargs):
        q = request.GET.get('q') if request.GET.get('q') is not None else ""
        print("q: ", q)
        data_with_q = list(filter(lambda news: q in news['title'], data))
        return render(request, "news/news_page.html", context={'data': data_with_q})


class CreatePage(View):
    def get(self, request, *args, **kwargs):
        return render(request, "news/create_page.html")
    
    def post(self, request, *args, **kwargs):
        created = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        text = request.POST.get('text')
        title = request.POST.get('title')
        
        all_links = sorted([news['link'] for news in data])
        for existing_link in all_links:
            if existing_link + 1 not in all_links:
                link = existing_link + 1
                break
        
        new_news = {"created": created, "text": text, "title": title, "link": link}
        data.append(new_news)
        
        with open(settings.NEWS_JSON_PATH, 'w') as data_file:
            json.dump(data, data_file)
        
        return redirect('/news')


class SpecificNewsPage(View):
    def get(self, request, link, *args, **kwargs):
        context = {}
        for item in data:
            if item['link'] == int(link):
                context = item
                break
        if not context:
            raise Http404
        return render(request, "news/specific_news_page.html", context=context)

