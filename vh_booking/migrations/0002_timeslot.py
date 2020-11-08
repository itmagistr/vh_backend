# Generated by Django 3.1.2 on 2020-11-01 20:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('vh_booking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('dt_start', models.TimeField(verbose_name='время начала промежутка')),
                ('dt_end', models.TimeField(verbose_name='время завершения промежутка')),
                ('descr', models.TextField(blank=True, null=True, verbose_name='описание временного промежутка')),
            ],
            options={
                'verbose_name': 'Временный промежуток',
                'verbose_name_plural': 'Временные промежутки',
            },
        ),
    ]
