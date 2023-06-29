from django.db import models


class New(models.Model):
    img = models.ImageField("Yangilikga oid rasm")
    title_uz = models.CharField('Yangilikning Sarlavhasi o\'zbek tilida', max_length=512)
    title_ru = models.CharField('Yangilikning Sarlavhai rus tilida', max_length=512)
    title_en = models.CharField('Yangilikning Sarlavha ingliz tilida', max_length=512)
    short_desc_uz = models.TextField("Yangilikning Qisqa ma'lumoti o'zbek tilida")
    short_desc_ru = models.TextField("Yangilikning Qisqa ma'lumoti rus tilida")
    short_desc_en = models.TextField("Yangilikning Qisqa ma'lumoti ingliz tilida")
    desc_uz = models.TextField("Yangilikning To'liq ma'lumoti o'zbek tilida")
    desc_ru = models.TextField("Yangilikning To'liq ma'lumoti rus tilida")
    desc_en = models.TextField("Yangilikning To'liq ma'lumoti ingliz tilida")
    date = models.DateField("Yangilikni saytga joylash vaqti", auto_now_add=True)

    def __str__(self):
        return self.title_uz
