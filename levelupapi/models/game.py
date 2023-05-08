from django.db import models

class Game(models.Model):

    title = models.CharField(max_length=50)
    maker = models.CharField(max_length=50)
    number_of_players = models.IntegerField()
    skill_level = models.IntegerField()
    game_type = models.ForeignKey(
        "GameType", on_delete=models.CASCADE, related_name='submitted_games')
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name='submitted_player')

# The on_delete parameter specifies what should happen to the Game object
# if the related GameType or Gamer object is deleted
# In this case, models.CASCADE is used,
# which means that if the related object is deleted,
# the Game object will also be deleted.
