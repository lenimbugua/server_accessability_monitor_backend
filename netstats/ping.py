import subprocess
import time
from random import choice
from .create_excel_file import write_into_file
from celery import shared_task


NO_OF_PACKETS = ['2', '1', '2', '2', '1' '1', '1', '1']
SLEEP_TIME = 2
PING_DURATION = 10


def calculate_next_ping_time(func):

    remaining_duration = PING_DURATION
    file_data = []

    def inner1(*args, **kwargs):
        while remaining_duration > 0:
            starttime = time.time()
            file_data.append(func(choice(NO_OF_PACKETS), *args))
            time.sleep(SLEEP_TIME)
            time_spent = time.time()-starttime
            remaining_duration = remaining_duration-time_spent
        write_into_file(
            file_data,  connection_name=kwargs['connection_name'],  uuid=kwargs['uuid'])
        return file_data

    return inner1


@shared_task
@calculate_next_ping_time
def ping(packets, ip_address, **kwargs):
    ping_time = time.ctime()
    try:
        response = subprocess.check_output(
            ['ping', '-c', packets, ip_address],
            stderr=subprocess.STDOUT,  # get all output
            universal_newlines=True  # return string not bytes
        )
        packets_transmitted = int(
            response[response.index('packets transmitted')-2])
        packets_received = int(response[response.index('packets received')-2])

        string_start = response.index('stddev = ')+9
        mini, average, maxi, stddev = list(
            response[string_start:-3].split("/"))

        try:
            packet_loss = (
                (packets_transmitted-packets_received)/packets_transmitted)*100
        except ZeroDivisionError:
            packet_loss = 0  # no packet was transmitted

        return ping_time, packets_transmitted, packets_received, packet_loss, mini, average, maxi, stddev

    except subprocess.CalledProcessError:
        server_not_found = "server not found"
        return ping_time, server_not_found, server_not_found,  server_not_found, server_not_found, server_not_found, server_not_found, server_not_found
