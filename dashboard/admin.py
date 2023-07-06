from django.contrib import admin

from dashboard.models import Patient, Retsep, Diagnoz, Files

# Register your models here.


admin.site.register(Patient)
admin.site.register(Retsep)
admin.site.register(Diagnoz)
admin.site.register(Files)
