from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

def index4(request):
    return render(request, 'Fourth task/index.html')


def shop4(request):
    context = {
        'items': ['Игровое золото', 'Помощь с прокачкой', 'Помощь в освоении рейдового контента'],
    }
    return render(request, 'Fourth task/shop.html', context)


def cart4(request):
    return render(request, 'Fourth task/cart.html')
