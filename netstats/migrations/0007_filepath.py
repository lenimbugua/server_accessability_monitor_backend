# Generated by Django 2.2.6 on 2019-10-15 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netstats', '0006_stats_connection_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilePath',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('connection_name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]