# Generated by Django 2.1.5 on 2019-02-09 10:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('players', '0034_auto_20190204_1440'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('image', models.ImageField(upload_to='images')),
                ('desc', models.CharField(blank=True, max_length=300)),
                ('price', models.FloatField()),
                ('rating', models.IntegerField()),
                ('no_of_rating', models.IntegerField()),
                ('upload_time', models.DateField(auto_now_add=True)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]