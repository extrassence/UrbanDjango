from django.shortcuts import render
from django.views.generic import TemplateView


def func(request):
    return render(request, 'Second task/left.html')


class Clas(TemplateView):
    template_name = 'Second task/right.html'
