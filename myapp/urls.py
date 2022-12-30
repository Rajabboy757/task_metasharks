from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('item/<int:item_id>/', show_item, name='item'),
    path('menu/<int:menu_id>/', show_menu, name='menu'),
]
