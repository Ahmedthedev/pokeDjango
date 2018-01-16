from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=30)


class Pokemon(models.Model):
    type = models.ManyToManyField(Type)
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150)


class Image(models.Model):
    url = models.CharField(max_length=300)


class Trainer(models.Model):
    name = models.CharField(max_length=50, unique=True)
    gender = models.CharField(max_length=20)
    image = models.OneToOneField(Image)


class TrainerPokemon(models.Model):
    name = models.CharField(max_length=50)
    pokemon = models.ForeignKey(Pokemon)
    trainer = models.ForeignKey(Trainer)
    level = models.IntegerField()
