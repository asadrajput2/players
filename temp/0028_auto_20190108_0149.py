# Generated by Django 2.1.4 on 2019-01-07 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0027_auto_20190108_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='mins_left',
            field=models.FloatField(blank='true', default=29, null='true'),
        ),
    ]
