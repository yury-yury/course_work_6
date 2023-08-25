from django.db import models


class BlogEntry(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=100, verbose_name='Slug')
    content = models.TextField(verbose_name='Содержание')
    preview = models.ImageField(upload_to='blog', blank=True, verbose_name='Превью')
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    published = models.BooleanField(default=True, verbose_name='Признак публикации')
    views_count = models.IntegerField(default=0, verbose_name='Просмотры')

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        """
        The Meta class contains the common name of the model instance in the singular and plural used
        in the administration panel.
        """
        verbose_name: str = "Запись блога"
        verbose_name_plural: str = "Записи блога"
        ordering = ["-created_at"]

