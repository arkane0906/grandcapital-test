from django import template

register = template.Library()


@register.simple_tag
def draw_menu(menu_name):
    return 'menu' # TODO Написать модель Менюшки и импортнуть сюда