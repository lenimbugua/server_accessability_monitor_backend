# Generated by Django 2.2.6 on 2019-10-15 13:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('netstats', '0007_filepath'),
    ]

    operations = [
        migrations.AddField(
            model_name='filepath',
            name='file_path',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
