from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def features(request):
    return render(request, 'main/features.html')


def faq(request):
    return render(request, 'main/faq.html')


def about(request):
    return render(request, 'main/about.html')


def login(request):
    return render(request, 'accounts/login.html')
