from django.http import HttpResponse
from django.shortcuts import  render

def index(request):
    return render(request, 'polls/index.html', {})

def hello(request):
    return HttpResponse("Hello, world. You're at the polls index.")