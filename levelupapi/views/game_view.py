"""View module for handling requests about games"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Game


class GameView(ViewSet):
    """Level up game view"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for SINGLE game

        Returns:
            Response -- JSON serialized game
        """
        # db_cursor.execute(""" # SQL equivalent
        # select id, label
        # from levelupapi_game
        # where id = ?""",(pk,)
        # )
        game = Game.objects.get(pk=pk)
        serializer = GameSerializer(game)
        return Response(serializer.data, status=status.HTTP_200_OK)
        # equivalent to _set_headers and wfile.write functions


    def list(self, request):
        """Handle GET requests to get ALL games

        Returns:
            Response -- JSON serialized list of games
        """
        # select * from levelupapi_game; # SQL equivalent
        game = Game.objects.all()
        serializer = GameSerializer(game, many=True)
        return Response(serializer.data)

class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        """holds the configuration for the serializer
        """
        model = Game
        fields = ('id', 'title', 'maker', 'number_of_players', 'skill_level', 'game_type', 'gamer')
