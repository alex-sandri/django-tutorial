from django.db import models


class Lega(models.Model):
    nome = models.TextField()


class Sport(models.Model):
    nome = models.TextField()


class Specialità(models.Model):
    nome = models.TextField()
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)


class Squadra(models.Model):
    compagnia = models.PositiveSmallIntegerField()
    lega = models.ForeignKey(Lega, on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
