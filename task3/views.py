from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

def index(request):
    return render(request, 'Third task/index.html')


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


def func(request):
    return render(request, 'Second task/left.html')


class Clas(TemplateView):
    template_name = 'Second task/right.html'
