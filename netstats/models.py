from django.db import models


class Stats(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    connection_name = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=100)
    packets_transmitted = models.CharField(max_length=100)
    packets_received = models.CharField(max_length=100)
    packet_loss = models.CharField(max_length=100)
    mini = models.CharField(max_length=100)
    maxi = models.CharField(max_length=100)
    average = models.CharField(max_length=100)
    stddev = models.CharField(max_length=100)

    class Meta:
        ordering = ['created']


class FilePath(models.Model):
    created = models.DateField(auto_now_add=True)
    connection_name = models.CharField(max_length=100)
    file_path = models.CharField(max_length=100)

    class Meta:
        ordering = ['created']
