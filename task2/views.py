from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

def index(request):
    return render(request, 'index.html')

def shop(request):
    context = {
        'title': 'Бухта добрых клыкарров',
        'items': ['Игровое золото', 'Помощь с прокачкой', 'Помощь в освоении рейдового контента'],
    }
    return render(request, 'shop.html', context)


def cart(request):
    context = {
        'title': 'Бухта добрых клыкарров',
    }
    return render(request, 'cart.html', context)


def left_(request):
    return render(request, 'left.html')


class Right_(TemplateView):
    template_name = 'right.html'
