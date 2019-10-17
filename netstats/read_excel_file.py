# Reading an excel file
import xlrd


def read_file():
    # Give the location of the file
    # Todo: parametrize file path
    loc = ("92b44a8f-bfda-4ff7-b44f-0fd21bb7aead.xlsx")

    # To open Workbook
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)

    file_data = []

    # populate file data into a 2d list
    for i in range(sheet.ncols):
        file_data.append(sheet.row_values(i+1))

    data = {
        "data": file_data
    }

    return data
