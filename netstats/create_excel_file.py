import xlwt
from xlwt import Workbook


def write_into_file(**kwargs):
    workbook = xlwt.Workbook()

    sheet = workbook.add_sheet("Sheet Name")

    # Specifying style
    style = xlwt.easyxf('font: bold 1')

    # Specifying column
    sheet.write(0, 0, 'Date Created', style)
    sheet.write(0, 1, 'Connection Name', style)
    sheet.write(0, 2, 'Ip_address', style)
    sheet.write(0, 3, 'Packet Transmitted', style)
    sheet.write(0, 4, 'Packets Received', style)
    sheet.write(0, 5, 'Maxi', style)
    sheet.write(0, 6, 'Mini', style)
    sheet.write(0, 7, 'Average', style)
    sheet.write(0, 8, 'Stddev', style)
    x, y = 72, 9
    for i in range(x):
        for j in range(y):
            sheet.write(i+1, j, 'x, y')
            if j > 8:
                break

    workbook.save("sample1.xlsx")
