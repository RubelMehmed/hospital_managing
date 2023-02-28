from django import forms

from .models import AVAIL_CHOICES, Appointment, Department, Doctor, Patient


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient_name', 'department', 'doctor', 'appointment_date', 'appointment_time']
        widgets = {
            'appointment_date': forms.HiddenInput(),
            'appointment_time': forms.HiddenInput(),
        }

    patient_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your full name'}))
    department = forms.ModelChoiceField(queryset=Department.objects.all(), empty_label='Select department')
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all(), empty_label='Select doctor')
    appointment_date = forms.DateField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    appointment_time = forms.ChoiceField(choices=AVAIL_CHOICES)

#py manage.py makemigrations