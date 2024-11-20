from django.db import models


class Lega(models.Model):
    nome = models.TextField()

    def __str__(self) -> str:
        return self.nome


class Sport(models.Model):
    nome = models.TextField()

    def __str__(self) -> str:
        return self.nome


class Specialità(models.Model):
    nome = models.TextField()
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.nome} ({self.sport})'


class Squadra(models.Model):
    compagnia = models.PositiveSmallIntegerField()
    lega = models.ForeignKey(Lega, on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.compagnia} - {self.lega} ({self.sport})'
