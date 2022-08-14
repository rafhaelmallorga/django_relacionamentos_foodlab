from django.db import models


class Seasons(models.TextChoices):
    SUMMER = "Verão"
    AUTUMN = "Outono"
    WINTER = "Inverno"
    SPRING = "Primavera"
    DEFAULT = "Não especificado"


class User(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField()
    favorite_season = models.CharField(
        max_length=20, choices=Seasons.choices, default=Seasons.DEFAULT
    )

    def __repr__(self) -> str:
        return f"<{self.id} - {self.email}>"
