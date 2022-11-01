# Generated by Django 4.1.3 on 2022-11-01 22:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0002_alter_car_manufacturer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='drivers',
            field=models.ManyToManyField(related_name='cars', to=settings.AUTH_USER_MODEL),
        ),
    ]
