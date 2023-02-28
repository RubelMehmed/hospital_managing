from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('department-list/', views.department_list, name='department_list'),
    path('department/<int:department_id>/doctors/', views.doctor_list, name='doctor_list'),
    path('doctor/<int:doctor_id>/schedule/', views.schedule, name='schedule'),
    path('appointment-form/', views.appointment_form, name='appointment_form'),
    path('appointment-confirmation/', views.appointment_confirmation, name='appointment_confirmation'),
]
