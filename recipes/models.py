from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    instructions = models.TextField(null=True, blank=True)

    # FK 1:N
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="recipes", null=True
    )

    def __repr__(self) -> str:
        return f"Recipe {self.id} - {self.name}"
