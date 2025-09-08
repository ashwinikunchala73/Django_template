from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render




# html page

def show_html(request):
    return render(request, "home.html")

def info_html(request):
    return render(request, "contactform.html")


def topiclist_page(request):
    return render(request, "topic.html")