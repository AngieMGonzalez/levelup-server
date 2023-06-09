"""View module for handling requests about events"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Event, Game, Gamer
from rest_framework.decorators import action

class EventView(ViewSet):
    """Level up event view"""

    @action(methods=['post'], detail=True)
    def signup(self, request, pk):
        """Post request for a user to sign up for an event"""

        gamer = Gamer.objects.get(user=request.auth.user)
        event = Event.objects.get(pk=pk)
        event.attendees.add(gamer)
        return Response({'message': 'Gamer added'}, status=status.HTTP_201_CREATED)

    @action(methods=['delete'], detail=True)
    def leave(self, request, pk):
        """Post request for a user to sign up for an event"""

        gamer = Gamer.objects.get(user=request.auth.user)
        event = Event.objects.get(pk=pk)
        event.attendees.remove(gamer)
        return Response({'message': 'Gamer Removed'}, status=status.HTTP_204_NO_CONTENT)



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
        This is the method that will be called when a
        GET request is made to the URL associated with this viewset
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

        # Set the `joined` property on every event
        for event in events:
            # Check to see if the gamer is in the attendees list on the event
            gamer = Gamer.objects.get(user=request.auth.user)
            # logic just for one user
            # event.joined will either be T/F
            # if the logged in gamer is attendees array on this event
            event.joined = gamer in event.attendees.all()

        # This line creates an instance of the EventSerializer class,
        # passing in the events queryset as the data to be serialized
        # The many=True argument specifies that there are multiple Event objects to be serialized
        serializer = EventSerializer(events, many=True)

        # This line returns an HTTP response with the serialized data
        # The Response class is provided by Django REST framework
        # and the serializer.data attribute contains
        # the serialized representation of the events queryset
        return Response(serializer.data)

    def update(self, request, pk=None):
        """Handle PUT requests for an event -entire obj

        Returns:
            Response -- Empty body with 204 status code
        """

        event = Event.objects.get(pk=pk)
        event.description = request.data["description"]
        event.date = request.data["date"]
        event.time = request.data["time"]

        game = Game.objects.get(pk=request.data["game"])
        event.game = game
        event.save()

        # no host? no atendees?

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """destroy / delete a row from DB
        """
        event = Event.objects.get(pk=pk)
        event.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)



class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for events
    """
    class Meta:
        """holds the configuration for the serializer
        """
        model = Event
        fields = ('id', 'description', 'date', 'time', 'game', 'host', 'attendees', 'joined')
        depth = 2
# fix this depth later
