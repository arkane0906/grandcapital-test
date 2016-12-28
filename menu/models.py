from django.db import models
from .utils import calc_positions


class Menu(models.Model):
    name = models.CharField(verbose_name='Название', max_length=100)

    def root_items(self):
        return MenuItem.objects.filter(menu=self, level=1).order_by('position')

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(verbose_name='Название', max_length=100)
    url = models.CharField(verbose_name='Адрес ссылки', max_length=250)
    menu = models.ForeignKey(Menu, verbose_name='Меню', on_delete=models.CASCADE, blank=True, null=True)
    parent = models.ForeignKey('self', verbose_name='Родительский пункт меню', on_delete=models.CASCADE,
                               blank=True, null=True)
    level = models.PositiveSmallIntegerField(verbose_name='Уровень', default=1)
    position = models.PositiveSmallIntegerField(verbose_name='Позиция', default=1)

    def child_items(self):
        return MenuItem.objects.filter(parent=self).order_by('position')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Menu item"
        verbose_name_plural = "Menu items"

    def save(self, force_insert=False, **kwargs):

        if self.parent:
            self.level = self.parent.level + 1
        else:
            self.level = 1

        if self.pk:
            new_parent = self.parent
            old_parent = MenuItem.objects.get(pk=self.pk).parent
            if old_parent != new_parent:
                if new_parent:
                    calc_positions(new_parent.children())
                    self.rank = new_parent.children().count()+1
                super(MenuItem, self).save(force_insert, **kwargs)
                if old_parent:
                    calc_positions(old_parent.children())
            else:
                super(MenuItem, self).save(force_insert, **kwargs)
        else:
            super(MenuItem, self).save(force_insert, **kwargs)
