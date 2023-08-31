from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# запрос на отображение главной страницы сайта (index.html)
def index(request):
    return HttpResponse('Начать подключение!')