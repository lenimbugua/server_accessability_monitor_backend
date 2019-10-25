import subprocess
import time


def calculate_next_ping_time(func):

    # added arguments inside the inner1,
    # if function takes any arguments,
    # can be added like this.
    def inner1(*args, **kwargs):

        remaining_duration = 60
        file_data = []
        while remaining_duration > 0:
            # storing time before function execution
            print("tick")
            starttime = time.time()
            file_data.append(func(*args, **kwargs))
            time_spent = time.time()-starttime
            remaining_duration = remaining_duration-time_spent

            # storing time after function execution
            end = time.time()

        return file_data

    return inner1


@calculate_next_ping_time
def calc_net_stats(packets, ip_address):

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


print(calc_net_stats('2', 'google.com'))
