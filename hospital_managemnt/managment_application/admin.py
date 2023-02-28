from django.contrib import admin
from .models import Doctor, Department, Schedule, Patient,Appointment
# Register your models here.
admin.site.register(Doctor)
admin.site.register(Department)
admin.site.register(Schedule)
admin.site.register(Appointment)
admin.site.register(Patient)
