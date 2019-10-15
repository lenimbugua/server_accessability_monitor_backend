from .models import Stats
from .serializers import StatsSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .latency import calc_net_stats
from .create_excel_file import write_into_file


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

        queryset = self.get_queryset()
        packet_loss = ((packets_transmitted-packets_received) /
                       packets_transmitted) * 100
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

        write_into_file(data)

        serializer = StatsSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StatsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stats.objects.all()
    serializer_class = StatsSerializer
