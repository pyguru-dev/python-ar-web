# Generated by Django 3.2.9 on 2022-01-10 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joboffers', '0004_joboffer_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joboffer',
            name='short_description',
            field=models.TextField(max_length=200, verbose_name='Descripción corta'),
        ),
    ]
