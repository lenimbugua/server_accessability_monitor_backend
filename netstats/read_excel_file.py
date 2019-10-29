# Reading an excel file
import xlrd
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from .serializers import StatsSerializer


def read_file(uuid):
    # Give the location of the file
    file_path = settings.FILES_DIR
    loc = ("{}/{}.xlsx".format(file_path, uuid))

    # To open Workbook
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
