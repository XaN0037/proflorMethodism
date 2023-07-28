from django.urls import path
import os
from sayt.views import Main
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    eval(settings.WONDERFUL)
]
