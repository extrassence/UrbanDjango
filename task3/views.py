from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

def index3(request):
    return render(request, 'Third task/index3.html')


def shop(request):
    context = {
        'title': 'Бухта добрых клыкарров',
        'items': ['Игровое золото', 'Помощь с прокачкой', 'Помощь в освоении рейдового контента'],
    }
    return render(request, 'Third task/shop.html', context)


def cart(request):
    context = {
        'title': 'Бухта добрых клыкарров',
    }
    return render(request, 'Third task/cart.html', context)
