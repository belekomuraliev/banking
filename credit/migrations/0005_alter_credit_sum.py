# Generated by Django 3.2 on 2022-11-09 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0004_auto_20221109_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credit',
            name='sum',
            field=models.IntegerField(blank=True, max_length=50, null=True),
        ),
    ]
