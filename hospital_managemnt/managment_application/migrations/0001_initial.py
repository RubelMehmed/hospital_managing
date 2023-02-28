# Generated by Django 3.2.5 on 2023-02-28 07:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(choices=[('Cardiologist', 'Cardiologist'), ('Dermatologists', 'Dermatologists'), ('Emergency Medicine Specialists', 'Emergency Medicine Specialists'), ('Allergists/Immunologists', 'Allergists/Immunologists'), ('Anesthesiologists', 'Anesthesiologists'), ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons')], default='Cardiologist', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_name', models.CharField(max_length=100)),
                ('d_dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='managment_application.department')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_date', models.DateField(max_length=20, verbose_name='date')),
                ('day_name', models.CharField(choices=[('1', 'Saturday'), ('2', 'Sunday'), ('3', 'Monday'), ('4', 'Tuesday'), ('5', 'Wednesday'), ('6', 'Thursday'), ('7', 'Friday')], max_length=20)),
                ('slot1', models.CharField(choices=[('available', 'AVAILABLE'), ('booked', 'BOOKED')], default='available', max_length=20, verbose_name='10 AM')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='managment_application.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=40)),
                ('mobile', models.CharField(max_length=20)),
                ('symptoms', models.CharField(max_length=100)),
                ('assign_date', models.DateField(auto_now=True)),
                ('assigned_doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='managment_application.doctor')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=False)),
                ('appointment_date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments_date', to='managment_application.schedule')),
                ('appointment_time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments_time', to='managment_application.schedule')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='managment_application.department')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='managment_application.doctor')),
            ],
        ),
    ]