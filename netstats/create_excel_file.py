import xlwt
from xlwt import Workbook
from django.conf import settings
from celery import shared_task


@shared_task
def write_into_file(data, unique_name, connection_name):
    """
    creates an excel file
    """
    file_path = settings.FILES_DIR
    workbook = xlwt.Workbook()

    sheet = workbook.add_sheet("{} connection".format(connection_name))

    # Specifying style
    style = xlwt.easyxf('font: bold 1')

    # Specifying column names
    sheet.write(0, 0, 'Connection Name', style)
    sheet.write(0, 1, 'Ip_address', style)
    sheet.write(0, 2, 'Packet Transmitted', style)
    sheet.write(0, 3, 'Packets Received', style)
    sheet.write(0, 4, 'Packet Loss', style)
    sheet.write(0, 5, 'Maxi', style)
    sheet.write(0, 6, 'Mini', style)
    sheet.write(0, 7, 'Average', style)
    sheet.write(0, 8, 'Stddev', style)
    x, y = 9, 0
    for i in range(x):
        for item in data.values():
            sheet.write(i+1, y, item)
            y += 1
            if y >= 9:
                y = 0
                break

    workbook.save(
        "{}/{}.xlsx".format(file_path, unique_name))
