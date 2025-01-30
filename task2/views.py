from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


def left_(request):
    return render(request, 'left.html')

class Right_(TemplateView):
    template_name = 'right.html'