from django.db import models


class Pizza(models.Model):

    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField(help_text='указывайте цену в сомах')
    image = models.ImageField(upload_to='pizza_images/')
    consist = models.TextField(verbose_name='состав')
    is_new = models.BooleanField()
    size = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField(verbose_name='вес в граммах')

    class Meta:
        verbose_name_plural = 'Пиццы'
        verbose_name = 'Пицца'
