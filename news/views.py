from urllib import request

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import News
from .forms import NewsForm
from django.utils import timezone
from django.contrib import messages


def index(request):
    news = News.objects.order_by('-create_time')
    context = {'news': news}
    return render(request, 'news/index.html', context)

@login_required(login_url='/login/')
def add(request):
    if request.method == 'POST':
        news = NewsForm(request.POST)
        if news.is_valid():
            news = news.save(commit=False)
            # news.author = request.user
            news.create_time = timezone.now()
            news.last_edit_time = timezone.now()
            news.save()
            return redirect('view_news')
        else:
            context = {'form': news}
            return render(request, 'news/add.html', context)
    else:
        news = NewsForm()
        context = {'form': news}
        return render(request, 'news/add.html', context)

@login_required(login_url='/login/')
def displaydata(request):
    results = News.objects.all()
    return render(request,"news/editnews.html",{"News":results})

def editnews(request,id):
    displaynews=News.objects.get(id=id)
    return render(request,"news/edit.html",{"news":displaynews})

def updatenews(request,id):
    updatenews= News.objects.get(id=id)
    form=NewsForm(request.POST, instance=updatenews)
    if form.is_valid:
        form.save()
        messages.success(request,"Record Updated Successfully...!")
        return render(request,"news/edit.html",{"news":updatenews})


def get(request, id):
     news = get_object_or_404(News, id=id)
     context = {'news': news}
     return render(request, 'news/view.html', context)
