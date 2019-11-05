from .models import Stats, FilePath
from .serializers import StatsSerializer, FilePathSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .read_excel_file import read_file
from .ping import ping
import uuid
from warnings import warn
from .calculate_time import schedule_ping


class Ping(generics.ListCreateAPIView):
    queryset = Stats.objects.all()
    serializer_class = StatsSerializer

    def create(self, request, format=None):
        request_data = request.data
        connection_name = request_data['connection_name']
        ip_address = request_data['ip_address']
        date = request_data['date']
        start_time = request_data['start_time']
        finish_time = request_data['finish_time']

        file_unique_name = str(uuid.uuid4())

        if ip_address == "" or connection_name == "" or date == None or start_time == None or finish_time == None:
            return Response("", status=status.HTTP_400_BAD_REQUEST)

        seconds_to_execution, duration = schedule_ping(
            date, start_time, finish_time)

        ping.apply_async([ip_address], {'duration': duration, 'connection_name': connection_name, 'uuid': file_unique_name},
                         countdown=3)

        file_path_serializer = FilePathSerializer(
            data={"connection_name": connection_name, "file_path": file_unique_name, "ip_address": ip_address})
        if file_path_serializer.is_valid():
            file_path_serializer.save()
            return Response(file_path_serializer.data, status=status.HTTP_201_CREATED)
        return Response(file_path_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FilePathList(generics.ListCreateAPIView):
    queryset = FilePath.objects.all()
    serializer_class = FilePathSerializer


class FileDetail(generics.RetrieveAPIView):

    def retrieve(self, request, *args, **kwargs):
        uuid = self.kwargs['uuid']
        return Response(read_file(uuid))
