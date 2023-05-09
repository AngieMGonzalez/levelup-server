"""View module for handling requests about events"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Event, Game, Gamer


class EventView(ViewSet):
    """Level up event view"""

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """

        gamer = Gamer.objects.get(user=request.auth.user)
        game = Game.objects.get(pk=request.data["game"])

        event = Event.objects.create(
            description=request.data["description"],
            date=request.data["date"],
            time=request.data["time"],
            host=gamer,
            game=game
        )

        # Add attendees to the event
        # attendee_ids = request.data.getlist("attendees")
        # attendees = Gamer.objects.filter(id__in=attendee_ids)
        # event.attendees.set(attendees)

        serializer = EventSerializer(event)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

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
        This is the method that will be called when a GET request is made to the URL associated with this viewset
        It takes in two arguments, self and request

        Returns:
            Response -- JSON serialized list of events
        """
        # This line retrieves all the Event objects from the 
        # database using the Django Object-Relational Mapping (ORM) system
        events = Event.objects.all()

        # This code block checks if the GET request has
        # a query parameter named game
        # If it does, it sets the variable game_id
        # to the value of the query parameter
        # Then it filters the events queryset 
        # to include only events where the game_id matches the game_id variable
        if "game" in request.query_params:
            game_id=request.query_params["game"]
            events = events.filter(game_id=game_id)

        # This line creates an instance of the EventSerializer class,
        # passing in the events queryset as the data to be serialized
        # The many=True argument specifies that there are multiple Event objects to be serialized
        serializer = EventSerializer(events, many=True)

        # This line returns an HTTP response with the serialized data
        # The Response class is provided by Django REST framework
        # and the serializer.data attribute contains
        # the serialized representation of the events queryset
        return Response(serializer.data)

class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for events
    """
    class Meta:
        """holds the configuration for the serializer
        """
        model = Event
        fields = ('id', 'description', 'date', 'time', 'game', 'host', 'attendees')
        depth = 1
# fix this depth later
