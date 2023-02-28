from django.shortcuts import get_object_or_404, render

from .appointment_form import AppointmentForm
from .models import AVAIL_CHOICES, Department, Doctor, Schedule


def appointment_form(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            patient = Patient.objects.get(user=request.user)
            appointment = form.save(commit=False)
            appointment.patient_name = patient.user.first_name + ' ' + patient.user.last_name
            appointment.save()
            form.save_m2m()
            return render(request, 'appointment_confirmation.html', {'appointment': appointment})
    else:
        form = AppointmentForm()

    schedules = Schedule.objects.filter(slot1=AVAIL_CHOICES[1]).order_by('s_date')
    context = {
        'form': form,
        'schedules': schedules,
    }
    return render(request, 'appointment_form.html', context)


def home(request):
    return render(request, 'home.html', {})



def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department_list.html', {'departments': departments})

def doctor_list(request, department_id):
    departments = get_object_or_404(Department, pk=department_id)
    doctors = Doctor.objects.filter(d_dept=departments)
    return render(request, 'doctor_list.html', {'departments': departments, 'doctors': doctors})

def schedule(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    schedules = Schedule.objects.filter(doctor=doctor)

    context = {
        'doctor': doctor,
        'schedules': schedules
    }
    return render(request, 'schedule.html', context)


def appointment_confirmation(request):
    return render(request, 'appointment_confirmation.html')

