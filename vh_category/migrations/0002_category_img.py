# Generated by Django 3.1.8 on 2021-06-02 21:30

from django.db import migrations, models
import vh_category.models


class Migration(migrations.Migration):

    dependencies = [
        ('vh_category', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=vh_category.models.image_upload_to),
        ),
    ]
