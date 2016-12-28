from django.contrib import admin
from menu.models import MenuItem
from django.db.models import Q


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'parent', 'level', 'position')
    readonly_fields = ('level', 'position')

    def render_change_form(self, request, context, *args, **kwargs):
        # Исключим из выбора родительского элемента текущий элемент (если он уже сохранен и имеет id)
        context['adminform'].form.fields['parent'].queryset = MenuItem.objects.filter(~Q(id=context['object_id']))
        return super(MenuItemAdmin, self).render_change_form(request, context, args, kwargs)

admin.site.register(MenuItem, MenuItemAdmin)
