# Generated by Django 2.2.4 on 2019-08-23 00:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20190821_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helpformmodel',
            name='when',
            field=models.DateField(default=datetime.datetime(2019, 8, 23, 0, 0, 35, 715281, tzinfo=utc)),
        ),
    ]
