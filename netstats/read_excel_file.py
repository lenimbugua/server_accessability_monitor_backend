# Reading an excel file
import xlrd
from pathlib import Path


def read_file(uuid):
    # Give the location of the file
    loc = Path("files/{}.xlsx".format(uuid))

    # Try to open Workbook
    try:
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_index(0)
        file_data = []

        # populate file data into a 2d list
        for i in range(sheet.nrows - 1):
            file_data.append(sheet.row_values(i+1))

        data = {
            "data": file_data
        }

        return data
    except FileNotFoundError:
        data = {
            "data": "Still Pinging"
        }
        return data
