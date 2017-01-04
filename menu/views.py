from django.http import HttpResponse, Http404
from django.template import loader

from .models import MenuItem


def menu(request):
	menu_items = MenuItem.objects.all()
	template = loader.get_template('menu/index.html')
	context = {
		'menu_items': menu_items,
	}
	return HttpResponse(template.render(context, request))


def show_page(request, menu_item_url):
	try:
		menu_item = MenuItem.objects.get(url=menu_item_url)
	except MenuItem.DoesNotExist:
		raise Http404('Menu item with URL  "/%s" does not exist.' % menu_item_url)
	template = loader.get_template('menu/page.html')
	context = {
		'menu_item': menu_item,
	}
	return HttpResponse(template.render(context, request))
