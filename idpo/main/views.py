from django.shortcuts import render
from .models import News, Сourses


def index(request):
    courses = Сourses.objects.all()
    news = News.objects.order_by('-date')[:5]
    return render(request, 'main/index.html', {'courses': courses, 'news': news})


def about(request):
    return render(request, 'main/about.html')

def course(request,id):
    get_artc = Сourses.objects.get(id=id)
    context = {
        'get_artc': get_artc
    }
    template ='main/course.html'

    return render(request, template, context)

def news(request,id):
    get_artc = News.objects.get(id=id)
    context = {
        'get_artc': get_artc
    }
    template ='main/news.html'

    return render(request, template, context)


