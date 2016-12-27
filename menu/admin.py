from django.contrib import admin
from menu.models import MenuItem
from django.db.models import Q


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'parent')

    def render_change_form(self, request, context, *args, **kwargs):
        context['adminform'].form.fields['parent'].queryset = MenuItem.objects.filter(~Q(id=1))
        return super(MenuItemAdmin, self).render_change_form(request, context, args, kwargs)

admin.site.register(MenuItem, MenuItemAdmin)
