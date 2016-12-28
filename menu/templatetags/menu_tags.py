from django import template
from menu.models import Menu, MenuItem

register = template.Library()


def draw_menu(context, menu_name):
    try:
        menu = Menu.objects.get(name=menu_name)
    except Menu.DoesNotExist:
        return context
    context['menu'] = menu
    context['menu_name'] = menu_name
    return context
register.inclusion_tag('menu/menu.html', takes_context=True)(draw_menu)


def draw_menu_item(context, menu_item):
    context['menu_item'] = menu_item
    return context
register.inclusion_tag('menu/menu_item.html', takes_context=True)(draw_menu_item)
