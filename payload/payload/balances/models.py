from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Balance(models.Model):
    name = models.CharField(max_length=100)
    value = models.TextField()

    def __str__(self):
        return self.name

