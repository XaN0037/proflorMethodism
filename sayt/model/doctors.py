
from django.db import models




class Doctor(models.Model):
    name_uz = models.CharField('Ismi o\'zbek tilida',max_length=128)
    first_name_uz = models.CharField("Familiyasi o'zbek tilida",max_length=128)
    middle_name_uz = models.CharField('Otasini ismi o\'zbek tilida',max_length=128)
    name_ru = models.CharField('Ismi rus',max_length=128)
    first_name_ru = models.CharField("Familiyasi rus tilida",max_length=128)
    middle_name_ru = models.CharField('Otasini ismi rus tilida',max_length=128)
    name_en = models.CharField('Ismi ingliz tilida',max_length=128)
    first_name_en = models.CharField("Familiyasi ingliz tildia",max_length=128)
    middle_name_en = models.CharField('Otasini ismi ingliz tilida',max_length=128)
    specialty_uz = models.CharField('Mutaxassisligi o\'zbek tilida',max_length=256)
    specialty_ru = models.CharField('Mutaxassisligi rus tilida',max_length=256)
    specialty_en = models.CharField('Mutaxassisligi ingliz tilida',max_length=256)
    about_doctor_uz = models.TextField('Shifokor haqida o\'zbek tilida')
    about_doctor_ru = models.TextField('Shifokor haqida rus tilida')
    about_doctor_en = models.TextField('Shifokor haqida ingliz tilida')
    phone = models.CharField('Shaxsiy Telefon raqam', max_length=25,null=True,blank=True)
    email = models.CharField('Shaxsiy Email sissilka', max_length=256,null=True,blank=True)
    instagramm = models.CharField('Shaxsiy Instagram sissilka', max_length=256,null=True,blank=True)
    telegram = models.CharField('Shaxsiy Telegram sissilka', max_length=256,null=True,blank=True)
    facebook = models.CharField('Shaxsiy Facebook sissilka', max_length=256,null=True,blank=True)
    twitter = models.CharField('Shaxsiy Twitter sissilka', max_length=256,null=True,blank=True)
    odnoklassniki = models.CharField('Shaxsiy Ok.ru sissilka', max_length=256,null=True,blank=True)
    img = models.ImageField('Shifokor sur\'ati')


    def __str__(self):
        return f"{self.name_uz} {self.first_name_uz}"
