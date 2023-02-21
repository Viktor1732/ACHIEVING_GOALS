from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Контент')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Изображение', null=True)
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    def __str__(self):
        return self.title
