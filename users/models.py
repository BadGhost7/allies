from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    discord = models.CharField(max_length=50, blank=True)
    steam_profile = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    def __str__(self):
        return f"Профиль {self.user.username}"




class Game(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='game_logos/', null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


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
text = models.TextField(null=True, blank=True)  

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField('О себе', blank=True)
    game_preferences = models.CharField('Игровые предпочтения', max_length=255, blank=True)
    skill_level = models.CharField('Уровень навыков', max_length=50, blank=True)
    is_public = models.BooleanField('Публичная анкета', default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def _str_(self):
        return f'Анкета {self.user.username}'

    class Meta:
        verbose_name = 'Анкета пользователя'
        verbose_name_plural = 'Анкеты пользователей'