from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=50)
    number = models.IntegerField()
    complement = models.CharField(max_length=50, null=True, blank=True)

    # FK 1:1
    user = models.OneToOneField("users.User", on_delete=models.CASCADE)
