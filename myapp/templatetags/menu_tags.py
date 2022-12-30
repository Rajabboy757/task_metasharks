from django import template
from myapp.models import *

register = template.Library()

@register.simple_tag(name='getmenus')
def get_menus(filter=None):
    if not filter:
        return Menu.objects.all()
    else:
        return Menu.objects.filter(pk=filter)

@register.inclusion_tag('list_menus.html')
def draw_menu(sort='name', menu_selected=0):
    if not sort:
        menu = Menu.objects.all()
    else:
        menu = Menu.objects.order_by(sort)

    return {"menu": menu, "menu_selected": menu_selected}
