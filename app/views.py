from django.shortcuts import render

# Create your views here.

def blog(request):
    return render(request,'blog.html')

def login(request):
    return render(request,"login.html")