# Generated by Django 3.2 on 2022-11-09 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0005_alter_credit_sum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
