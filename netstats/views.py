from .models import Stats, FilePath
from .serializers import StatsSerializer, FilePathSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .latency import calc_net_stats
from .create_excel_file import write_into_file
from .read_excel_file import read_file
import uuid


class StatsList(generics.ListCreateAPIView):
    queryset = Stats.objects.all()
    serializer_class = StatsSerializer

    def create(self, request, format=None):
        request_data = request.data
        connection_name = request_data['connection_name']
        ip_address = request_data['ip_address']
        packets = request_data['packets']

        if (packets or ip_address) == "":
            return Response("", status=status.HTTP_400_BAD_REQUEST)

        if calc_net_stats(packets, ip_address) is not None:
            packets_transmitted, packets_received, mini, average, maxi, stddev = calc_net_stats(
                packets, ip_address)
        else:
            return Response("", status=status.HTTP_417_EXPECTATION_FAILED)
        try:
            packet_loss = ((packets_transmitted-packets_received) /
                           packets_transmitted) * 100
        except ZeroDivisionError:
            packet_loss = "No packet was transmitted"

        queryset = self.get_queryset()

        data = {
            "connection_name": connection_name,
            "ip_address": ip_address,
            "packets_transmitted": packets_transmitted,
            "packets_received": packets_received,
            "packet_loss": packet_loss,
            "mini": mini,
            "maxi": maxi,
            "average": average,
            "stddev": stddev,
        }
        file_unique_name = str(uuid.uuid4())
        write_into_file(data, file_unique_name, connection_name)

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
