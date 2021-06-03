# Generated by Django 3.1.8 on 2021-06-03 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vh_employee', '0001_initial'),
        ('vh_product', '0003_producthuman'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductHuman',
            new_name='ProductEmployee',
        ),
        migrations.RemoveField(
            model_name='productemployee',
            name='human',
        ),
        migrations.AddField(
            model_name='productemployee',
            name='employee',
            field=models.ForeignKey(blank=True, help_text='Веберите исполнителя продукта', null=True, on_delete=django.db.models.deletion.CASCADE, to='vh_employee.employee', verbose_name='Исполнитель'),
        ),
    ]
