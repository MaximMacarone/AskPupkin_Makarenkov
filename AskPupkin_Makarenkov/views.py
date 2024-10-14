from django.http import HttpResponse, request
from django.shortcuts import render

def base(request):
    return render(request, 'static/base.html')