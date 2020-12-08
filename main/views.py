from django.shortcuts import render

def index(request):
    return render(request,"templates_website/index.html")
