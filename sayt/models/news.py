from django.db import models
import os
from django.dispatch import receiver


class New(models.Model):
    image = models.ImageField("Yangilikga oid rasm", upload_to='image_sayt_news')
    title_uz = models.CharField('Yangilikning Sarlavhasi o\'zbek tilida', max_length=512)
    title_ru = models.CharField('Yangilikning Sarlavhai rus tilida', max_length=512)
    short_desc_uz = models.TextField("Yangilikning Qisqa ma'lumoti o'zbek tilida")
    short_desc_ru = models.TextField("Yangilikning Qisqa ma'lumoti rus tilida")
    desc_uz = models.TextField("Yangilikning To'liq ma'lumoti o'zbek tilida")
    desc_ru = models.TextField("Yangilikning To'liq ma'lumoti rus tilida")
    date = models.DateField("Yangilikni saytga joylash vaqti", auto_now_add=True)

    def __str__(self):
        return self.title_uz

    def save(self, *args, **kwargs):
        if self.pk:
            previous_instance = New.objects.get(pk=self.pk)
            if self.image != previous_instance.image:
                if os.path.isfile(previous_instance.image.path):
                    os.remove(previous_instance.image.path)

        # Save the new file
        super().save(*args, **kwargs)


@receiver(models.signals.pre_delete, sender=New)
def delete_diagnostic_files(sender, instance, **kwargs):
    if instance.image:
        if os.path.exists(instance.image.path):
            os.remove(instance.image.path)

    # title_en = models.CharField('Yangilikning Sarlavha ingliz tilida', max_length=512)
    # short_desc_en = models.TextField("Yangilikning Qisqa ma'lumoti ingliz tilida")

# desc_en = models.TextField("Yangilikning To'liq ma'lumoti ingliz tilida")
