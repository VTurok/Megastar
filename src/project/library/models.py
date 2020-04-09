from django.db import models


class Writer(models.Model):
    name = models.CharField(verbose_name="Автор", max_length=40, blank=False, db_index=True)


class Book(models.Model):
    author_id = models.ForeignKey(Writer, related_name='books', on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Название книги", max_length=150, blank=False, db_index=True)

