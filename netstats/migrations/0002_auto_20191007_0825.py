# Generated by Django 2.2.6 on 2019-10-07 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netstats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stats',
            name='ip_address',
            field=models.CharField(default='localhost', max_length=255),
        ),
        migrations.AddField(
            model_name='stats',
            name='packets',
            field=models.IntegerField(default=3),
        ),
    ]
