from .models import Stats, FilePath
from .serializers import StatsSerializer, FilePathSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .read_excel_file import read_file
import uuid


class StatsList(generics.ListCreateAPIView):
    queryset = Stats.objects.all()
    serializer_class = StatsSerializer

    def create(self, request, format=None):
        request_data = request.data
        connection_name = request_data['connection_name']
        ip_address = request_data['ip_address']

        if (ip_address) == "":
            return Response("", status=status.HTTP_400_BAD_REQUEST)

        file_unique_name = str(uuid.uuid4())
        # write_into_file.apply_async(
        #     [data, file_unique_name, connection_name], countdown=0, expires=20)

        file_path_serializer = FilePathSerializer(
            data={"connection_name": connection_name, "file_path": file_unique_name, "ip_address": ip_address})
        if file_path_serializer.is_valid():
            file_path_serializer.save()
            return Response(file_path_serializer.data, status=status.HTTP_201_CREATED)
        return Response(file_path_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StatsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stats.objects.all()
    serializer_class = StatsSerializer


class FilePathList(generics.ListCreateAPIView):
    queryset = FilePath.objects.all()
    serializer_class = FilePathSerializer


class FileDetail(generics.RetrieveAPIView):

    def retrieve(self, request, *args, **kwargs):
        uuid = self.kwargs['uuid']
        return Response(read_file(uuid))
