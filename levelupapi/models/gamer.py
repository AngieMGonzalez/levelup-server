from django.db import models
from django.contrib.auth.models import User
# user, a 1 to 1 is considered a foreign key
class Gamer(models.Model):
    # Relationship to the built-in User model which has name and email
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Additional bio field to capture from the client
    bio = models.CharField(max_length=155)

    @property # decorator
    def full_name(self):
        """Additional field to capture from the client"""
        return f'{self.user.first_name} {self.user.last_name}'
