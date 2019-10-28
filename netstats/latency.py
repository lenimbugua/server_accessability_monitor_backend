import subprocess
import time
from random import choice
from create_excel_file import write_into_file

NO_OF_PACKETS = ['5', '5', '7', '8', '8' '9', '10', '15']
SLEEP_TIME = 30


def calculate_next_ping_time(func):

    def inner1(*args, **kwargs):
        print(kwargs)
        remaining_duration = 3
        file_data = []
        while remaining_duration > 0:

            starttime = time.time()
            file_data.append(func(choice(NO_OF_PACKETS), *args))
            # time.sleep(SLEEP_TIME)
            time_spent = time.time()-starttime
            remaining_duration = remaining_duration-time_spent
        write_into_file(file_data, kwargs['connection_name'], kwargs['uuid'])
        return file_data

    return inner1


@calculate_next_ping_time
def calc_net_stats(packets, ip_address, **kwargs):

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

        return packets_transmitted, packets_received, mini, average, maxi, stddev

    except subprocess.CalledProcessError:
        response = None


print(calc_net_stats('google.com', connection_name="google", uuid="82783465jfjghjfg"))
