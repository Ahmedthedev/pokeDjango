from rest_framework import  serializers
from pokeDjangoRestApi.models import *

#
# class Type(models.Model):
#     name = models.CharField(max_length=30)
#
#
# class Pokemon(models.Model):
#     type = models.ManyToManyField(Type)
#     name = models.CharField(max_length=50, unique=True)
#     description = models.CharField(max_length=150)
#
#
# class Image(models.Model):
#     url = models.CharField(max_length=300)
#
#
# class Trainer(models.Model):
#     name = models.CharField(max_length=50, unique=True)
#     gender = models.CharField(max_length=20)
#     image = models.OneToOneField(Image)
#
#
# class TrainerPokemon(models.Model):
#     name = models.CharField(max_length=50)
#     pokemon = models.ForeignKey(Pokemon)
#     trainer = models.ForeignKey(Trainer)
#     level = models.IntegerField()
#
#

class PokemonSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Pokemon
        fields = ('name', 'description')


class TrainerPokemonSerializer(serializers.ModelSerializer) :
    class Meta:
        model = TrainerPokemon
        fields = ('name', 'pokemon', 'trainer', 'level')


class TrainerSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Trainer
        fields = ('name', 'gender', 'image')


class TypeSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Type
        fields = ('name',)


class ImageSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Image
        fields = ('url',) #ça buguait jusqu'à ce que j'ajoute la virgule ...