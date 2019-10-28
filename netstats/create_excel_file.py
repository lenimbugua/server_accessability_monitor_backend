import xlwt
from xlwt import Workbook
from django.conf import settings
# from celery import shared_task


# @shared_task
def write_into_file(data, unique_name, connection_name):
    """
    creates an excel file
    """
    # file_path = settings.FILES_DIR
    file_path = "/Users/len/Documents/wraptious/server_accessability_monitor/netstats/files"
    workbook = xlwt.Workbook()

    sheet = workbook.add_sheet("{} connection".format(connection_name))

    # Specifying style
    style = xlwt.easyxf('font: bold 1')

    # Specifying column names
    # headers = ['name', 'foo']

    # for i in range(len(headers)):
    #     sheet.write(0, i, headers[i], style)

    sheet.write(0, 0, 'Connection Name', style)
    sheet.write(0, 1, 'Ip_address', style)
    sheet.write(0, 2, 'Time', style)
    sheet.write(0, 3, 'Packet Transmitted', style)
    sheet.write(0, 4, 'Packets Received', style)
    sheet.write(0, 5, 'Packet Loss', style)
    sheet.write(0, 6, 'Maxi', style)
    sheet.write(0, 7, 'Mini', style)
    sheet.write(0, 8, 'Average', style)
    sheet.write(0, 9, 'Stddev', style)

    y = 0
    for i in data:

        sheet.write(y+1, y, i[y])
        y += 1
        if y >= 9:
            y = 0
            break

    workbook.save(
        "{}/{}.xlsx".format(file_path, unique_name))

    return '0'
