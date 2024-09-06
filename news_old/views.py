"""
from django.shortcuts import render
# Create your views here.
def news(request):
    return render(request, 'news.html')
"""

from django.shortcuts import render
from .models import News
def news(request):
    newss = News.objects.all().order_by('-date')
    return render(request, 'news.html', {'newss':newss})    

from .models import News
def news(request):
    newss = News.objects.all().order_by('-date')
    return render(request, 'news.html', {'newss':newss})
