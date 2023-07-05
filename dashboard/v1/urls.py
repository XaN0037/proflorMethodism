from django.urls import path
import os
from dashboard.views import Main
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    eval(settings.UNIQUE)
]
