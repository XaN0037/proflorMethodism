from django.contrib import admin

from dashboard.models import Patient, Retsep, Diagnoz

# Register your models here.


admin.site.register(Patient)
admin.site.register(Retsep)
admin.site.register(Diagnoz)
