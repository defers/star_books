from django.db import models
import star_books.utils.string_utils as string_utils
from django.contrib import admin
from django.contrib.auth.models import User

# class User(models.Model):
#     id = models.AutoField(verbose_name="id", primary_key=True, editable=False)
#     name = models.CharField(verbose_name="name", max_length=150)
#     email = models.EmailField(verbose_name="email")
#
#     def __str__(self):
#         text = string_utils.get_class_representation(self.__dict__)
#         return f"{self.__class__.__name__}: {text}"


class Author(models.Model):
    id = models.AutoField(verbose_name="id", primary_key=True, editable=False)
    name = models.CharField(verbose_name="name", max_length=150)

    def __str__(self):
        text = string_utils.get_class_representation(self.__dict__)
        return f"{self.__class__.__name__}: {text}"


class Book(models.Model):
    id = models.AutoField(verbose_name="id", primary_key=True, editable=False)
    name = models.CharField(verbose_name="name", max_length=250)
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE,
                               verbose_name="author_id", related_name="authors")

    def __str__(self):
        text = string_utils.get_class_representation(self.__dict__)
        return f"{self.__class__.__name__}: {text}"

