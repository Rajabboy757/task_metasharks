from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *


def index(request):

    context = {
        'title': 'Главная страница',
        'menu_selected': 0,
    }

    return render(request, 'index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_item(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")


def show_menu(request, menu_id):
    menu_items = MenuItem.objects.filter(menu_id=menu_id).order_by('name')

    if len(menu_items) == 0:
        raise Http404()

    context = {
        'menu_items': menu_items,
        'menu_selected': menu_id,
    }

    return render(request, 'index.html', context=context)
