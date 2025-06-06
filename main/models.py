from django.db import models
from django.contrib.auth.models import User
class Post(models.Model):
    title = models.CharField("Заголовок", max_length=120)
    text = models.TextField("Текст")
    created_at = models.DateField("дата создания", auto_now_add=True)
    image = models.ImageField("изображение", upload_to="posts/",blank=True, null=True)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def _str_(self):
        return self.title
    

class Game (models.Model):
    title = models.CharField("Название игры", max_length=100)
    cover = models.ImageField("обложка игры", upload_to="game_covers/")
    users = models.ManyToManyField(User, verbose_name="Игроки", related_name="games")

    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"

    def _str_(self):
        return self.title


class Questionnaire (models.Model):
    nickname = models.CharField("Ник", max_length=60, blank=True, help_text="Оставьте поле пустым, чтобы применить никнейи из стима")
    hours = models.FloatField("Наиграно часов")
    rang = models.CharField("Ранг", max_length=30, blank=True, null=True)
    user = models.ForeignKey(User, verbose_name="Игрок", related_name="Questionnaires", on_delete=models.CASCADE)
    game = models.ForeignKey(Game, verbose_name="Игра", related_name="Questionnaires", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.nickname:
            self.nickname = self.user.profile.nickname
        return super().save(*args, **kwargs)