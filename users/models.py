from django.contrib.auth.models import User
from django.db import models

# Профиль пользователя 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    discord = models.CharField(max_length=50, blank=True)
    steam_profile = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Профиль {self.user.username}"

# Игра
class Game(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='game_logos/', null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

# Анкета для поиска команды
class Anketa(models.Model):
    RANK_CHOICES = [
        ('beginner', 'Новичок'),
        ('average', 'Средний'),
        ('pro', 'Профессионал'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    rank = models.CharField(max_length=20, choices=RANK_CHOICES)
    about_me = models.TextField()
    play_style = models.CharField(max_length=100)
    looking_for = models.TextField(help_text="Кого ищете в команду?")
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Анкета {self.user.username} ({self.game.name})"
text = models.TextField(null=True, blank=True)  # Разрешить NULL значения