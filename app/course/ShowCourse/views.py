from django.shortcuts import render
import requests
from .script import *

def Hello(request):
    
    n = price


    return render(request, 'ShowCourse/index.html', context = {'name' : n})
