# Generated by Django 3.2.15 on 2024-01-28 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0055_auto_20240128_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(db_index=True, max_length=100, verbose_name='адрес'),
        ),
        migrations.AlterField(
            model_name='order',
            name='firstname',
            field=models.CharField(max_length=100, verbose_name='имя'),
        ),
        migrations.AlterField(
            model_name='order',
            name='lastname',
            field=models.CharField(max_length=100, verbose_name='фамилия'),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.CharField(choices=[('CASH', 'Наличные'), ('CARD', 'Электронно')], db_index=True, default='Электронно', max_length=100, verbose_name='способ оплаты'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('FS', 'Обработанный'), ('PR', 'Необработанный')], db_index=True, default='Необработанный', max_length=100, verbose_name='статус'),
        ),
    ]