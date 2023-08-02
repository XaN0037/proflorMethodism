import os

from django.db import models
from django.dispatch import receiver


class Doctor(models.Model):
    name_uz = models.CharField('Ismi o\'zbek tilida', max_length=128, null=True, blank=True)
    name_ru = models.CharField('Ismi rus', max_length=128, null=True, blank=True)
    name_en = models.CharField('Ismi ingliz tilida', max_length=128, null=True, blank=True)
    first_name_uz = models.CharField("Familiyasi o'zbek tilida", max_length=128, null=True, blank=True)
    first_name_ru = models.CharField("Familiyasi rus tilida", max_length=128, null=True, blank=True)
    first_name_en = models.CharField("Familiyasi ingliz tildia", max_length=128, null=True, blank=True)
    middle_name_uz = models.CharField('Otasini ismi o\'zbek tilida', max_length=128, null=True, blank=True)
    middle_name_ru = models.CharField('Otasini ismi rus tilida', max_length=128, null=True, blank=True)
    middle_name_en = models.CharField('Otasini ismi ingliz tilida', max_length=128, null=True, blank=True)
    specialty_uz = models.CharField('Mutaxassisligi o\'zbek tilida', max_length=256, null=True, blank=True)
    specialty_ru = models.CharField('Mutaxassisligi rus tilida', max_length=256, null=True, blank=True)
    specialty_en = models.CharField('Mutaxassisligi ingliz tilida', max_length=256, null=True, blank=True)
    about_doctor_uz = models.TextField('Shifokor haqida o\'zbek tilida', null=True, blank=True)
    about_doctor_ru = models.TextField('Shifokor haqida rus tilida', null=True, blank=True)
    about_doctor_en = models.TextField('Shifokor haqida ingliz tilida', null=True, blank=True)
    phone = models.CharField('Shaxsiy Telefon raqam', max_length=25, null=True, blank=True)
    email = models.CharField('Shaxsiy Email sissilka', max_length=256, null=True, blank=True)
    instagramm = models.CharField('Shaxsiy Instagram sissilka', max_length=256, null=True, blank=True)
    telegram = models.CharField('Shaxsiy Telegram sissilka', max_length=256, null=True, blank=True)
    facebook = models.CharField('Shaxsiy Facebook sissilka', max_length=256, null=True, blank=True)
    twitter = models.CharField('Shaxsiy Twitter sissilka', max_length=256, null=True, blank=True)
    odnoklassniki = models.CharField('Shaxsiy Ok.ru sissilka', max_length=256, null=True, blank=True)
    image = models.ImageField('Shifokor sur\'ati',upload_to='image_sayt_doctors')

    def __str__(self):
        return f"{self.name_uz} {self.first_name_uz}"

    def save(self, *args, **kwargs):
        if self.pk:
            previous_instance = Doctor.objects.get(pk=self.pk)
            if self.image != previous_instance.image:
                if os.path.isfile(previous_instance.image.path):
                    os.remove(previous_instance.image.path)

        # Save the new file
        super().save(*args, **kwargs)

@receiver(models.signals.pre_delete, sender=Doctor)
def delete_diagnostic_files(sender, instance, **kwargs):
    if instance.image:
        if os.path.exists(instance.image.path):
            os.remove(instance.image.path)
