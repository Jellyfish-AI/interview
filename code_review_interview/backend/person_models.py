from django.db import models


class Person(models.Model):

    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=64, unique=True)