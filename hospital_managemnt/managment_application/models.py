from django.contrib.auth.models import User
from django.db import models

#Department now only =>


departments = [
    ('Cardiologist', 'Cardiologist'),
    ('Dermatologists', 'Dermatologists'),
    ('Emergency Medicine Specialists', 'Emergency Medicine Specialists'),
    ('Allergists/Immunologists', 'Allergists/Immunologists'),
    ('Anesthesiologists', 'Anesthesiologists'),
    ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons'),
]

class Department(models.Model):
    department_id = models.IntegerField(null=True)
    department = models.CharField(max_length=50, choices=departments, default='Cardiologist')

    def __str__(self):
        return f"{self.department} Department"


#Doctor only => 
class Doctor(models.Model):
    doctor_id = models.IntegerField(null=True)
    d_name = models.CharField(max_length=100)
    d_dept = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.d_name

#Schedule only => 


WEEKLY_DAY = (
    ("1", "Saturday"),
    ("2", "Sunday"),
    ("3", "Monday"),
    ("4", "Tuesday"),
    ("5", "Wednesday"),
    ("6", "Thursday"),
    ("7", "Friday"),
)

AVAIL_CHOICES = (
    ('available', 'AVAILABLE'),
    ('booked', 'BOOKED'),
)

class Schedule(models.Model):
    s_date = models.DateField(max_length=20, verbose_name='date')
    day_name = models.CharField(max_length=20, choices=WEEKLY_DAY)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    slot1 = models.CharField(max_length=20, choices=AVAIL_CHOICES, default='available', verbose_name='10 AM')

#patient only =>

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=False)
    symptoms = models.CharField(max_length=100, null=False)
    assigned_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    assign_date = models.DateField(auto_now=True)

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return self.user.first_name + " (" + self.symptoms + ")"

#Appointment only => 
class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name='appointments_date')
    appointment_time = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name='appointments_time')
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.patient_name} - {self.department.department} - {self.doctor.d_name} - {self.appointment_date.s_date} - {self.appointment_time.slot1}"
