from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    age = models.IntegerField()

    def __str__(self) -> str:
        return self.name
        