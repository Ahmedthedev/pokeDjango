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
from rest_framework.parsers import JSONParser
from rest_framework.exceptions import ParseError

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
        try:
            data = JSONParser().parse(request)
        except ParseError:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
        serializer = PokemonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return HttpResponse(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def pokemonsById(request, pokemon_id):
    if request.method == 'GET':
        try:
            pokemon = Pokemon.objects.get(pk=pokemon_id)
            serializer = PokemonSerializer(pokemon, many=False)
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
        except Pokemon.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)     
    
    elif request.method == 'PUT':
        try:
            j = json.loads(request.body)
            pokemon = Pokemon.objects.filter(pk=pokemon_id)
            response = pokemon.update(name=j["name"])
            if response == 0 :
                return HttpResponse(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return HttpResponse(status=status.HTTP_200_OK)
        except Pokemon.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        
    elif request.method == 'DELETE':
        try:
            print("delete")
            print(pokemon_id)
            pokemon = Pokemon.objects.get(pk=pokemon_id)
            pokemon.pk = pokemon_id
            pokemon.delete()
            return HttpResponse(status=status.HTTP_200_OK)
        except Pokemon.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

### TrainerPokemon

@csrf_exempt
def pokemonsTrainers(request):
    if request.method == 'GET':
        trainers = TrainerPokemon.objects.all()
        serializer = TrainerPokemonSerializer(trainers, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        return HttpResponse(status=status.HTTP_200_OK)

@csrf_exempt
def pokemonsTrainersById(request, pokemonsTrainers_id):
    if request.method == 'GET':
        try:
            pokemonsTrainers = TrainerPokemon.objects.get(pk=pokemonsTrainers_id)
            serializer = TrainerPokemonSerializer(pokemonsTrainers, many=False)
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
        except TrainerPokemon.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    elif request.method == 'PUT':
        return HttpResponse(status=status.HTTP_200_OK)



### Trainer

@csrf_exempt
def trainers(request):
    if request.method == 'GET':
        trainers = Trainer.objects.all()
        serializer = TrainerSerializer(trainers, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        return HttpResponse(status=status.HTTP_200_OK)

@csrf_exempt
def trainersById(request, trainers_id):
    if request.method == 'GET':
        try:
            trainer = Trainer.objects.get(pk=trainers_id)
            serializer = TrainerSerializer(trainer, many=False)
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
        except Trainer.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'PUT':
        return HttpResponse(status=status.HTTP_200_OK)



### Types

@csrf_exempt
def types(request):
    if request.method == 'GET':
        types = Type.objects.all()
        serializer = TypeSerializer(types, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        return HttpResponse(status=status.HTTP_200_OK)

@csrf_exempt
def typesById(request, types_id):
    if request.method == 'GET':
        try:
            pokeType = Type.objects.get(pk=types_id)
            serializer = TypeSerializer(pokeType, many=False)
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
        except Type.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        
    elif request.method == 'PUT':
        return HttpResponse(status=status.HTTP_200_OK)