from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Hellow Wrold, You are at My Home Page.")
    return render(request, 'website\index.html')

def about(request):
    return HttpResponse("Hellow Wrold, You are at My About Page.")

def contact(request):
    return HttpResponse("Hellow Wrold, You are at My Contact Page.")
