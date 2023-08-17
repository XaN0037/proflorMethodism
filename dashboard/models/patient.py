import os

from django.conf import settings
from django.db import models
from django.dispatch import receiver


class Patient(models.Model):
    name = models.CharField('Bemorning Ismi', max_length=128)
    first_name = models.CharField('Bemorning Familiyasi', max_length=128)
    father_name = models.CharField('Otasining ismi', max_length=128, null=True, blank=True)
    age = models.CharField('Bemorning tug\'ilgan yili', max_length=4, null=True, blank=True)
    phone = models.CharField('Bemorning telefon raqami', max_length=16, null=True, blank=True)
    """Comment faqat bazaga yoziladi, qog'ozda chiqarilmaydi"""
    comment = models.TextField("Izox", null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.first_name}"


class Files(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    file = models.FileField(upload_to='document_patient/')

    def __str__(self):
        return f"{self.patient.name}"

    """File ni o'zgartirganda fileni django projectdan o'chirib keyin qaytadan yangi fileni yozib qo'yadi"""

    def save(self, *args, **kwargs):
        if self.pk:
            previous_instance = Files.objects.get(pk=self.pk)
            if self.file != previous_instance.file:
                if os.path.isfile(previous_instance.file.path):
                    os.remove(previous_instance.file.path)

        # Save the new file
        super().save(*args, **kwargs)


class Diagnoz(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    diagnoz = models.TextField('Tashxis')
    recommendation = models.TextField('Tavsiya',null=True, blank=True)
    """Comment faqat bazaga yoziladi, qog'ozda chiqarilmaydi"""
    comment = models.TextField("Izox", null=True, blank=True)
    date = models.DateField(auto_now=True,null=True,blank=True)
    image_one = models.ImageField('Birinchi rasm', null=True, blank=True, upload_to="image_diagnoz/")
    image_two = models.ImageField('Ikkinchi rasm', null=True, blank=True, upload_to="image_diagnoz/")

    def save(self, *args, **kwargs):
        if self.pk:
            previous_instance = Diagnoz.objects.get(pk=self.pk)
            if self.image_one != previous_instance.image_one:
                if os.path.isfile(previous_instance.image_one.path):
                    os.remove(previous_instance.image_one.path)
            if self.image_two != previous_instance.image_two:
                if os.path.isfile(previous_instance.image_two.path):
                    os.remove(previous_instance.image_two.path)

        # Save the new file
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.patient} :::::: Diagnoz:   {self.diagnoz}"




"""File modelida fileni o'chirganda django projectdan ham o'chiradi"""


@receiver(models.signals.post_delete, sender=Files)
def delete_file(sender, instance, **kwargs):
    if instance.file:
        file_path = instance.file.path
        if os.path.exists(file_path):
            os.remove(file_path)


"""Diagnoz modelida rasmlarni o'chirganda django projectdan ham o'chiradi"""


@receiver(models.signals.pre_delete, sender=Diagnoz)
def delete_diagnostic_files(sender, instance, **kwargs):
    if instance.image_one:
        if os.path.exists(instance.image_one.path):
            os.remove(instance.image_one.path)
    if instance.image_two:
        if os.path.exists(instance.image_two.path):
            os.remove(instance.image_two.path)
