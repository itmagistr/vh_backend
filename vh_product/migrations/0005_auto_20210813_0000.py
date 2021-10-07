# Generated by Django 3.1.13 on 2021-08-12 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vh_employee', '0001_initial'),
        ('vh_product', '0004_auto_20210604_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title_check',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='title_check_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='title_check_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='productemployee',
            name='employee',
            field=models.ForeignKey(blank=True, help_text='Веберите исполнителя продукта', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='vh_employee.employee', verbose_name='Исполнитель'),
        ),
        migrations.AlterField(
            model_name='productemployee',
            name='product',
            field=models.ForeignKey(blank=True, help_text='Укажите продукт из каталога', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='workers', to='vh_product.product', verbose_name='Продукт'),
        ),
    ]