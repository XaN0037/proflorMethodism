from django.db import models


class Retsep(models.Model):
    name = models.CharField(max_length=256)
    info = models.TextField()

    def __str__(self):
        return self.name
