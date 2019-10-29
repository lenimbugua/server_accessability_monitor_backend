import xlwt
from xlwt import Workbook
from django.conf import settings


def write_into_file(data, **kwargs):
    """
    creates an excel file
    """
    file_path = settings.FILES_DIR
    workbook = xlwt.Workbook()

    sheet = workbook.add_sheet(kwargs['connection_name'])

    # Specifying style
    style = xlwt.easyxf('font: bold 1')

    # Specifying column names
    headers = ['Time', 'Packets Transmitted', 'Packets received',
               'Packet Loss', 'Maxi', 'Mini', 'Average', 'Stddv']

    for i in range(len(headers)):
        sheet.write(0, i, headers[i], style)
    print(data)
    x = 0
    for row in data:
        y = 0
        for item in row:
            sheet.write(x+1, y, item)
            y += 1
        x += 1

    workbook.save(
        "{}/{}.xlsx".format(file_path, kwargs['uuid']))
