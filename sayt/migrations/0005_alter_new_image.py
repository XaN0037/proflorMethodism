# Generated by Django 4.2.2 on 2023-08-02 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sayt', '0004_alter_new_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='image',
            field=models.ImageField(upload_to='image_sayt_news', verbose_name='Yangilikga oid rasm'),
        ),
    ]
