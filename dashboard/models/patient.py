import os

from django.conf import settings
from django.db import models
from django.dispatch import receiver


class Patient(models.Model):
    name = models.CharField('Bemorning Ismi', max_length=128)
    first_name = models.CharField('Bemorning Familiyasi', max_length=128)
    father_name = models.CharField('Otasining ismi', max_length=128)
    age = models.CharField('Bemorning tug\'ilgan yili', max_length=4)
    phone = models.CharField('Bemorning telefon raqami', max_length=16)
    """Comment faqat bazaga yoziladi, qog'ozda chiqarilmaydi"""
    comment = models.TextField("Izox")

    def __str__(self):
        return f"{self.name} {self.first_name}"


class Files(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    file = models.FileField(upload_to='document_patient/')

    def __str__(self):
        return f"{self.patient.name}"

    def save(self, *args, **kwargs):
        # Check if the instance already exists in the database
        if self.pk:
            # Get the previous instance from the database
            previous_instance = Files.objects.get(pk=self.pk)
            # Check if the file field has changed
            if self.file != previous_instance.file:
                # Delete the previous file from the project
                if os.path.isfile(previous_instance.file.path):
                    os.remove(previous_instance.file.path)

        # Save the new file
        super().save(*args, **kwargs)



class Diagnoz(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    diagnoz = models.TextField('Tashxis')
    recommendation = models.TextField('Tavsiya')
    """Comment faqat bazaga yoziladi, qog'ozda chiqarilmaydi"""
    comment = models.TextField("Izox")
    date = models.DateField(auto_now=True)
    image_one = models.ImageField('Birinchi rasm', null=True, blank=True, upload_to="image_diagnoz/")
    image_two = models.ImageField('Ikkinchi rasm', null=True, blank=True, upload_to="image_diagnoz/")

    def __str__(self):
        return f"{self.patient}{self.diagnoz}"


@receiver(models.signals.post_delete, sender=Files)
def delete_file(sender, instance, **kwargs):
    if instance.file:
        file_path = instance.file.path
        if os.path.exists(file_path):
            os.remove(file_path)


@receiver(models.signals.pre_delete, sender=Diagnoz)
def delete_diagnostic_files(sender, instance, **kwargs):
    if instance.image_one:
        if os.path.exists(instance.image_one.path):
            os.remove(instance.image_one.path)
    if instance.image_two:
        if os.path.exists(instance.image_two.path):
            os.remove(instance.image_two.path)
