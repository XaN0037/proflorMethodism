from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.shortcuts import render
from methodism import METHODISM

from sayt import methods


# Create your views here.


class Main(METHODISM):
    file = methods
    not_auth_methods = settings.METHODS
