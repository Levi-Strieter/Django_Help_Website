# Generated by Django 2.2.4 on 2019-08-26 00:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20190826_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faqformmodel',
            name='date_uploaded',
            field=models.DateField(default=datetime.datetime(2019, 8, 26, 0, 29, 41, 946017, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='helpformmodel',
            name='when',
            field=models.DateField(default=datetime.datetime(2019, 8, 26, 0, 29, 41, 945725, tzinfo=utc)),
        ),
    ]
