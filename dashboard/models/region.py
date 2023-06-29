from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=128)


class Didscrit(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    tuman = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.region.name} {self.tuman}"
