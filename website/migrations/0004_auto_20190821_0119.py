# Generated by Django 2.2.4 on 2019-08-21 01:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20190821_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helpformmodel',
            name='when',
            field=models.DateField(default=datetime.datetime(2019, 8, 21, 1, 19, 45, 252348, tzinfo=utc)),
        ),
    ]
