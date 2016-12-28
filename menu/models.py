from django.db import models


class Menu(models.Model):
    name = models.CharField(verbose_name='Название', max_length=100)

    def root_items(self):
        return MenuItem.objects.filter(menu=self, level=1)


class MenuItem(models.Model):
    name = models.CharField(verbose_name='Название', max_length=100)
    url = models.CharField(verbose_name='Адрес ссылки', max_length=250)
    menu = models.ForeignKey(Menu, verbose_name='Меню', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', verbose_name='Родительский пункт меню', on_delete=models.CASCADE,
                               blank=True, null=True)
    level = models.PositiveSmallIntegerField(verbose_name='Уровень', default=1)
    position = models.PositiveSmallIntegerField(verbose_name='Позиция', default=1)

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

        super(MenuItem, self).save()
