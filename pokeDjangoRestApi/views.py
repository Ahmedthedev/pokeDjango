# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework import  status
from .models import Pokemon, Type, Trainer, TrainerPokemon
from django.views.decorators.csrf import csrf_exempt
from pokeDjangoRestApi.serializers import *
from django.core import serializers
import json

from django.shortcuts import render

# Create your views here.

@csrf_exempt
def imgs(request):
    if request.method == 'POST':
        j = json.loads(request.body)
        p = Image(url=j["url"])
        p.save()
        return HttpResponse(status=status.HTTP_200_OK)

@csrf_exempt
def pokemons(request):
    if request.method == 'GET':
        pokemons = Pokemon.objects.all()
        serializer = PokemonSerializer(pokemons, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        j = json.loads(request.body)
        p = Pokemon(name=j["name"],description=j["description"])
        p.save()
        return HttpResponse(status=status.HTTP_200_OK)

def pokemonsById(request, pokemon_id):
    pokemon = Pokemon.objects.get(pk=pokemon_id)
    serializer = PokemonSerializer(pokemon, many=False)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)




def pokemonsTrainers(request):
    return HttpResponse(status=status.HTTP_200_OK)

def pokemonsTrainersById(request, pokemonsTrainers_id):
    pokemonsTrainers = PokemonTrainers.objects.get(pk=pokemonsTrainers_id)
    serializer = PokemonTrainersSerializer(pokemonsTrainers, many=False)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)




def trainers(request):
    return HttpResponse(status=status.HTTP_200_OK)

def trainersById(request, trainers_id):
    trainer = Trainer.objects.get(pk=trainers_id)
    serializer = TrainerSerializer(trainer, many=False)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)




def types(request):
    return HttpResponse(status=status.HTTP_200_OK)

def typesById(request, types_id):
    return HttpResponse(status=status.HTTP_200_OK)