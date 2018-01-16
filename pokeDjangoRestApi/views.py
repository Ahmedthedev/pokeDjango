# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework import  status
from .models import Pokemon
from django.views.decorators.csrf import csrf_exempt
from pokeDjangoRestApi.serializers import *
from django.core import serializers


from django.shortcuts import render

# Create your views here.

@csrf_exempt
def pokemons(request):
    if request.method == 'GET':
        pokemons = Pokemon.objects.all()
        serializer = PokemonSerializer(pokemons, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        pokemon = serializers.deserialize(Pokemon,request.body)
        pokemon.save()
        return HttpResponse(status=status.HTTP_200_OK)

def pokemonsById(request, pokemon_id):
    pokemon = Pokemon.objects.get(pk=pokemon_id)
    serializer = PokemonSerializer(pokemon, many=False)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)




def pokemonsTrainers(request):
    return HttpResponse(status=status.HTTP_200_OK)

def pokemonsTrainersById(request, pokemonsTrainers_id):
    return HttpResponse(status=status.HTTP_200_OK)




def trainers(request):
    return HttpResponse(status=status.HTTP_200_OK)

def trainersById(request, trainers_id):
    return HttpResponse(status=status.HTTP_200_OK)




def types(request):
    return HttpResponse(status=status.HTTP_200_OK)

def typesById(request, types_id):
    return HttpResponse(status=status.HTTP_200_OK)