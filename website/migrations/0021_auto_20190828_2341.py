# Generated by Django 2.2.4 on 2019-08-28 23:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0020_auto_20190828_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faqformmodel',
            name='date_uploaded',
            field=models.DateField(default=datetime.datetime(2019, 8, 28, 23, 41, 51, 705882, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='helpformmodel',
            name='date_uploaded',
            field=models.DateField(default=datetime.datetime(2019, 8, 28, 23, 41, 51, 705556, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='videoformmodel',
            name='vid_name',
            field=models.CharField(default='Core Help-', max_length=20),
        ),
    ]
