"""View module for handling requests about games"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Game, Gamer, GameType


class GameView(ViewSet):
    """Level up game view"""

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        # db_cursor.execute(""" # SQL equivalent
        # select *
        # from levelupapi_gamer
        # where user = ?
        # """, (user,))
        gamer = Gamer.objects.get(user=request.auth.user)
        game_type = GameType.objects.get(pk=request.data["gameTypeId"])

        # db_cursor.execute("""
        # Insert into levelupapi_game
        # (title, maker, number_of_players, skill_level, gamer_id, game_type_id)
        # values (?, ?, ?, ?, ?, ?)
        # """, (request.data["title"], request.data["maker"],
        # request.data["numberOfPlayers"], request.data["skillLevel"], gamer, game_type))

        game = Game.objects.create(
            # request.data grabs outside object
            title=request.data["title"],
            maker=request.data["maker"],
            number_of_players=request.data["numberOfPlayers"],
            skill_level=request.data["skillLevel"],
            gamer=gamer,
            game_type=game_type
        )
        serializer = GameSerializer(game)
        return Response(serializer.data, status.HTTP_201_CREATED)

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

        # for testing delete
        try:
            game = Game.objects.get(pk=pk)
            serializer = GameSerializer(game)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
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

    def update(self, request, pk=None):
        """Handle PUT requests for a game -entire obj

        Returns:
            Response -- Empty body with 204 status code
        """
        # has to match client request
        game = Game.objects.get(pk=pk)
        game.title = request.data["title"]
        game.maker = request.data["maker"]
        game.number_of_players = request.data["numberOfPlayers"]
        game.skill_level = request.data["skillLevel"]

        game_type = GameType.objects.get(pk=request.data["gameTypeId"])
        game.game_type = game_type
        game.save()
        # why no gamer? why isn't that necessary?
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """destroy / delete a row from DB
        """
        game = Game.objects.get(pk=pk)
        game.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        """holds the configuration for the serializer
        """
        model = Game
        fields = ('id', 'title', 'maker', 'number_of_players', 'skill_level', 'game_type', 'gamer')
