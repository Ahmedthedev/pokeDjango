# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, JsonResponse
from rest_framework import  status
from django.views.decorators.csrf import csrf_exempt
from pokeDjangoRestApi.serializers import *
import json
from rest_framework.parsers import JSONParser
from rest_framework.exceptions import ParseError

# Create your views here.


@csrf_exempt
def imgs(request):
    if request.method == 'GET':
        imgs = Image.objects.all()
        serializer = ImageSerializer(imgs, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        try:
            data = JSONParser().parse(request)
        except ParseError:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
        serializer = ImageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return HttpResponse(serializer.data, status=status.HTTP_400_BAD_REQUEST)


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
        try:
            data = JSONParser().parse(request)
        except ParseError:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
        serializer = TrainerPokemonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return HttpResponse(serializer.data, status=status.HTTP_400_BAD_REQUEST)


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
        j = json.loads(request.body)
        try:
            pokemonsTrainers = TrainerPokemon.objects.filter(pk=pokemonsTrainers_id)
            pokemon = Pokemon.objects.get(pk=j["pokemon"])
            trainer = Trainer.objects.get(pk=j["trainer"])
            resp = pokemonsTrainers.update(name=j["name"],pokemon=pokemon,trainer=trainer,level=j["level"])
            if resp == 0:
                return HttpResponse(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return HttpResponse(status=status.HTTP_200_OK)
        except (Trainer.DoesNotExist, Pokemon.DoesNotExist):
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        j = json.loads(request.body)
        try:
            pokemonsTrainers = TrainerPokemon.objects.filter(pk=pokemonsTrainers_id)
            pokemonsTrainers.delete()
            return HttpResponse(status=status.HTTP_200_OK)
        except (Trainer.DoesNotExist, Pokemon.DoesNotExist):
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)


### Trainer

@csrf_exempt
def trainers(request):
    if request.method == 'GET':
        trainers = Trainer.objects.all()
        serializer = TrainerSerializer(trainers, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        try:
            data = JSONParser().parse(request)
        except ParseError:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
        serializer = TrainerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return HttpResponse(serializer.data, status=status.HTTP_400_BAD_REQUEST)


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
        j = json.loads(request.body)
        try:
            trainer = Trainer.objects.filter(pk=trainers_id)
            resp = trainer.update(name=j["name"], gender=j["gender"], image=j["image"])
            if resp == 0:
                return HttpResponse(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return HttpResponse(status=status.HTTP_200_OK)
        except (Trainer.DoesNotExist, Pokemon.DoesNotExist):
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        try:
            trainer = Trainer.objects.get(pk=trainers_id)
            trainer.delete()
            return HttpResponse(status=status.HTTP_200_OK)
        except Trainer.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)


### Types

@csrf_exempt
def types(request):
    if request.method == 'GET':
        types = Type.objects.all()
        serializer = TypeSerializer(types, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        try:
            data = JSONParser().parse(request)
        except ParseError:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
        serializer = TypeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return HttpResponse(serializer.data, status=status.HTTP_400_BAD_REQUEST)


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
        try:
            j = json.loads(request.body)
            pokeType = Type.objects.filter(pk=types_id)
            response = pokeType.update(name=j["name"])
            if response == 0 :
                return HttpResponse(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return HttpResponse(status=status.HTTP_200_OK)
        except Type.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        try:
            pokeType = Type.objects.get(pk=types_id)
            pokeType.pk = types_id
            pokeType.delete()
            return HttpResponse(status=status.HTTP_200_OK)
        except Type.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)