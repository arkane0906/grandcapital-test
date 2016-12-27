from django.db import models


class MenuItem(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=100
    )
    url = models.CharField(
        verbose_name='Адрес ссылки',
        max_length=250,
        blank=True,
        null=True
    )
    parent = models.ForeignKey(
        'self',
        verbose_name='Родительский пункт меню',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    level = models.PositiveSmallIntegerField(
        verbose_name='Уровень',
        default=0,
        editable=False
    )
    position = models.PositiveSmallIntegerField(
        verbose_name='Позиция',
        default=0,
        editable=False
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Menu item"
        verbose_name_plural = "Menu items"

    def save(self, force_insert=False, **kwargs):

        if self.parent:
            self.level = self.parent.level + 1
        else:
            self.level = 0
