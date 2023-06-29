# from django.db import models
#
# # Create your models here.
# from django.contrib.auth.base_user import BaseUserManager
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# from django.utils import timezone
# from django.db import models
#
#
# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None, is_staff=False,
#                     is_active=True, **extra_fields):
#         'Creates a User with the given username, email and password'
#
#         user = self.model(phone=email, is_active=is_active,
#                           is_staff=is_staff, **extra_fields)
#
#         if password:
#             user.set_password(password)
#
#         user.save()
#         return user
#
#     def create_superuser(self, email, password=None, **extra_fields):
#         return self.create_user(email, password, is_staff=True,
#                                 is_superuser=True, **extra_fields)
#
#
# class User(AbstractBaseUser, PermissionsMixin):
#     nickname = models.CharField('nickname', max_length=200, blank=False, null=False, )
#     firstname_uz = models.CharField(max_length=200, blank=True, null=True, )
#     firstname_ru = models.CharField(max_length=200, blank=True, null=True, )
#     lastname_uz = models.CharField(max_length=200, blank=True, null=True, )
#     lastname_ru = models.CharField(max_length=200, blank=True, null=True, )
#     fathername_uz = models.CharField(max_length=200, blank=True, null=True, )
#     fathername_ru = models.CharField(max_length=200, blank=True, null=True, )
#     phone = models.CharField('User Phone', max_length=100, unique=True, blank=True, null=True)
#     email = models.CharField('User email',max_length=128, unique=True)
#     logo = models.ImageField('User logo')
#     photo = models.ImageField('User photo')
#
#     is_staff = models.BooleanField(default=False,)
#     is_active = models.BooleanField(default=True, null=False)
#     date_joined = models.DateTimeField(default=timezone.now, editable=False)
#
#     USERNAME_FIELD = "email"
#     objects = UserManager()
#
#     def __str__(self):
#         return self.email