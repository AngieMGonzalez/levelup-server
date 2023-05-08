"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import GameType


class GameTypeView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        # db_cursor.execute(""" # SQL equivalent
        # select id, label
        # from levelupapi_gametype
        # where id = ?""",(pk,)
        # )
        game_type = GameType.objects.get(pk=pk)
        serializer = GameTypeSerializer(game_type)
        return Response(serializer.data)
        # equivalent to _set_headers and wfile.write functions


    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        # select * from levelupapi_gametype; # SQL equivalent 
        game_types = GameType.objects.all()
        serializer = GameTypeSerializer(game_types, many=True)
        return Response(serializer.data)

class GameTypeSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        """holds the configuration for the serializer
        """
        model = GameType
        fields = ('id', 'label')
