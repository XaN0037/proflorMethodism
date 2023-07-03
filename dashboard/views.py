from django.shortcuts import render
from methodism import METHODISM
from .v1 import methods


# Create your views here.


class Main(METHODISM):
    file = methods
    not_auth_methods = ['patient_view',"patient_add","patient_change","patient_delete",
                        "retsep_view","retsep_add","retsep_change"

                       ]
