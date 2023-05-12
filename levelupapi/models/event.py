from django.db import models
from .gamer import Gamer

class Event(models.Model):

    description = models.CharField(max_length=155)
    date = models.DateField()
    time = models.TimeField()
    host = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name="hosted_events")
    attendees = models.ManyToManyField(Gamer, related_name="event_attendees")
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="events")

# The related_name parameter specifies the name of the reverse relation
# from the Game model to the Event model.
# In this case, the reverse relation can be accessed through Game.game_for_event.
# for "host" Gamer.organizer_or_host
# "attendees" Gamer.event_has_people.

# does not actually exist in DB
@property
def joined(self):
    """joining and leaving events
    """
    return self.__joined
# just declaring joined

@joined.setter
def joined(self, value):
    self.__joined = value
# setter func to assign value elsewhere
