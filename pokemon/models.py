from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField()

    hp = models.IntegerField()
    attack = models.IntegerField()

    height = models.IntegerField()
    weight = models.IntegerField()
    base_experience = models.IntegerField()

    types = models.CharField(max_length=100)
    abilities = models.CharField(max_length=200)

    def __str__(self):
        return self.name