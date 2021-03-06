# Generated by Django 3.1.8 on 2021-05-17 20:35

import datetime
from django.db import migrations, models
import vh_doctor.models


class Migration(migrations.Migration):

    dependencies = [
        ('vh_doctor', '0002_auto_20201201_2341'),
    ]

    operations = [
        migrations.AddField(
            model_name='special',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=vh_doctor.models.image_upload_to),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='dt_practic',
            field=models.DateField(default=datetime.datetime(2018, 5, 17, 23, 35, 0, 722357), help_text='Укажите дату начала медецинской практики', verbose_name='Дата начала практики'),
        ),
    ]
