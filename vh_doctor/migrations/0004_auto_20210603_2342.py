# Generated by Django 3.1.8 on 2021-06-03 20:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vh_doctor', '0003_auto_20210517_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='dt_practic',
            field=models.DateField(default=datetime.datetime(2018, 6, 3, 23, 42, 3, 498426), help_text='Укажите дату начала медецинской практики', verbose_name='Дата начала практики'),
        ),
    ]
