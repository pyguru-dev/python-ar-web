# Generated by Django 3.2.12 on 2022-06-07 19:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pycompanies', '0003_usercompanyprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercompanyprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company', to=settings.AUTH_USER_MODEL),
        ),
    ]
