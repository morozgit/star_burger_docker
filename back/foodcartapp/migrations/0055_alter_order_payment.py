# Generated by Django 3.2.15 on 2024-01-26 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0054_auto_20231212_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.CharField(choices=[('CASH', 'Наличные'), ('CARD', 'Электронно')], db_index=True, default='Электронно', max_length=30, verbose_name='способ оплаты'),
        ),
    ]
