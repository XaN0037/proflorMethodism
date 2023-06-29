from django.db import models


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


class Diagnoz(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    diagnoz = models.TextField('Tashxis')
    recommendation = models.TextField('Tavsiya')
    """Comment faqat bazaga yoziladi, qog'ozda chiqarilmaydi"""
    comment = models.TextField("Izox")
    date = models.DateField(auto_now=True)
    image_one = models.ImageField('Birinchi rasm')
    image_two = models.ImageField('Ikkinchi rasm')

    def __str__(self):
        return f"{self.patient}{self.diagnoz}"
