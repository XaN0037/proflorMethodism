from django.db import models


class Contact(models.Model):
    phone_mobile = models.CharField('Telefon raqam shaxsiy', max_length=25)
    phone_clinica = models.CharField('Telefon raqam clinica', max_length=25)
    email = models.CharField('Email sissilka', max_length=256, null=True, blank=True)
    adress_uz = models.CharField('Manzil so\'z bilan o\'zbek tilida', max_length=256, null=True, blank=True)
    adress_ru = models.CharField('Manzil so\'z bilan rus tilida', max_length=256, null=True, blank=True)
    adress_en = models.CharField('Manzil so\'z bilan ingliz tilida', max_length=256, null=True, blank=True)
    instagramm = models.CharField('Instagram sissilka', max_length=256, null=True, blank=True)
    telegram = models.CharField('Telegram sissilka', max_length=256, null=True, blank=True)
    facebook = models.CharField('Facebook sissilka', max_length=256, null=True, blank=True)
    twitter = models.CharField('Twitter sissilka', max_length=256, null=True, blank=True)
    odnoklassniki = models.CharField('Ok.ru sissilka', max_length=256, null=True, blank=True)
    youtube = models.CharField('YOUTUBE sissilka', max_length=256, null=True, blank=True)
    locatsiya = models.CharField('Locatsiya sissilka', max_length=256, null=True, blank=True)

    def save(self, *args, **kwargs):
        for i in Contact.objects.all():
            if self.id != i.id:
                i.delete()
        super(Contact,self).save(*args, **kwargs)
    def __str__(self):
        return f"Shaxsiy {self.phone_mobile}  Clinica{self.phone_clinica}"
