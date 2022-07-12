from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    return render(request, 'mooses/index.html', context)

def blog(request):
    context = {}
    return render(request, 'mooses/blog.html', context)

def about(request):
    context = {}
    return render(request, 'mooses/about.html', context)

def contact(request):
    context = {}
    return render(request, 'mooses/contact.html', context)
