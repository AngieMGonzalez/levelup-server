"""View module for handling requests about events"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Event


class EventView(ViewSet):
    """Level up event view"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for SINGLE event

        Returns:
            Response -- JSON serialized event
        """

        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data, status=status.HTTP_200_OK)
        # equivalent to _set_headers and wfile.write functions


    def list(self, request):
        """Handle GET requests to get ALL events

        Returns:
            Response -- JSON serialized list of events
        """
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for events
    """
    class Meta:
        """holds the configuration for the serializer
        """
        model = Event
        fields = ('id', 'description', 'date', 'time', 'game', 'host', 'attendees')
