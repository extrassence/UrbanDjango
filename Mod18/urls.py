"""
URL configuration for Mod18 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from example1.views import index
from task2.views import func, Clas
from task3.views import index3, shop, cart
from task4.views import index4, shop4, cart4
from task5.views import sign_up_by_html, sign_up_by_django

urlpatterns = [
    path('admin/', admin.site.urls),
    path('htmlform/', sign_up_by_html, name='htmf'),
    path('djangoform/', sign_up_by_django, name='djnf'),
    path('', index, name='index'),
    path('index3/', index3, name='index3'),
    path('shop/', shop, name='shop'),
    path('func/', func, name='func'),
    path('clas/', Clas.as_view(), name='clas'),
    path('index4/', index4, name='index4'),
    path('shop4/', shop4, name='shop4'),
    path('cart/', cart, name='cart'),
    path('cart4/', cart4, name='cart4')
]
