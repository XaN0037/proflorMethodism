from django.db import models


class Retsep(models.Model):
    name_uz = models.CharField('uz_name',max_length=256)
    name_ru = models.CharField('ru_name',max_length=256)
    info_uz = models.TextField('uz_info',null=True, blank=True)
    info_ru = models.TextField('ru_info',null=True, blank=True)

    def __str__(self):
        return self.name_ru
