# Generated by Django 4.2.2 on 2023-08-02 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sayt', '0008_doctor_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='is_staff',
        ),
    ]
