# Generated by Django 3.1.8 on 2021-06-03 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vh_medproc', '0002_auto_20210604_0123'),
    ]

    operations = [
        migrations.AddField(
            model_name='medproc',
            name='recomend_after_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='medproc',
            name='recomend_after_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='medproc',
            name='recomend_before_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='medproc',
            name='recomend_before_ru',
            field=models.TextField(blank=True, null=True),
        ),
    ]
