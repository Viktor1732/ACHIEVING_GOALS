from django.db import models
from django.urls import reverse


class Goals(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название цели')
    description = models.TextField(blank=True, verbose_name='Описание цели')
    category = models.CharField(max_length=100, verbose_name='Категория')
    time_of_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_of_end = models.DateTimeField(verbose_name='Дата завершения')
    image = models.ImageField(upload_to='photos/goals/%Y/%m/%d/', verbose_name='Изображение', null=True)
    is_published = models.BooleanField(default=False, verbose_name='Публикация')
    is_completed = models.BooleanField(default=False, verbose_name='Завершенность')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('goal', kwargs={'goal': self.title})


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name='Контент')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Изображение', null=True)
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news', kwargs={'news_slug': self.slug})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['time_create']
