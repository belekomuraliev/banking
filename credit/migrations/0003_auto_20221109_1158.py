# Generated by Django 3.2 on 2022-11-09 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0002_auto_20221109_1154'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': 'Счет', 'verbose_name_plural': 'Счета'},
        ),
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'Клиента', 'verbose_name_plural': 'Клиенты'},
        ),
        migrations.AlterModelOptions(
            name='credit',
            options={'verbose_name': 'Кредит', 'verbose_name_plural': 'Кредиты'},
        ),
    ]