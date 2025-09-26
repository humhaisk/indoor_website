from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Match(models.Model):
    GAME_CHOICES = [
        ('carrom', 'Carrom'),
        ('chess', 'Chess'),
        ('table_tennis', 'Table Tennis'),
        ('badminton', 'Badminton'),
    ]
    
    game = models.CharField(max_length=50, choices=GAME_CHOICES)
    player1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='player1_matches')
    player2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='player2_matches')
    score_player1 = models.IntegerField(default=0)
    score_player2 = models.IntegerField(default=0)
    is_live = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    winner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='won_matches')

    def __str__(self):
        return f"{self.game.capitalize()}: {self.player1} vs {self.player2}"