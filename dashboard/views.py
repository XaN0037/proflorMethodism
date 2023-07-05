from django.conf import settings
from django.shortcuts import render
from methodism import METHODISM
from .v1 import methods


# Create your views here.


class Main(METHODISM):
    file = methods
    print('not auth lllllllllllllllllllllllllllllllllllllllllllllllllll')
    not_auth_methods = settings.METHODS
    print('not auth twoo       lllllllllllllllllllllllllllllllllllllllllllllllllll')
