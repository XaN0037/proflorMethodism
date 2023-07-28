# Generated by Django 4.2.2 on 2023-07-28 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_alter_diagnoz_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='retsep',
            name='info',
        ),
        migrations.RemoveField(
            model_name='retsep',
            name='name',
        ),
        migrations.AddField(
            model_name='retsep',
            name='info_ru',
            field=models.TextField(blank=True, null=True, verbose_name='ru_info'),
        ),
        migrations.AddField(
            model_name='retsep',
            name='info_uz',
            field=models.TextField(blank=True, null=True, verbose_name='uz_info'),
        ),
        migrations.AddField(
            model_name='retsep',
            name='name_ru',
            field=models.CharField(default=1, max_length=256, verbose_name='ru_name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='retsep',
            name='name_uz',
            field=models.CharField(default=1, max_length=256, verbose_name='uz_name'),
            preserve_default=False,
        ),
    ]
