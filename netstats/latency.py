
import subprocess


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

        # try:
        #     packet_loss = (packets_transmitted-packets_received) / \
        #         packets_transmitted*100
        # except ZeroDivisionError:
        #     packet_loss = 0

    except subprocess.CalledProcessError:
        response = None
