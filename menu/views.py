from django.http import HttpResponse
from django.template import loader

from .models import MenuItem


def menu(request):
	menu_items = MenuItem.objects.all()
	template = loader.get_template('menu/index.html')
	context = {
		'menu_items': menu_items,
	}
	return HttpResponse(template.render(context, request))
