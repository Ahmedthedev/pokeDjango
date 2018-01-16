# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, JsonResponse
from rest_framework import  status
from .models import Pokemon
from pokeDjangoRestApi.serializers import *

from django.shortcuts import render

# Create your views here.
# url(r'^pokemons/$',views.pokemons),
# url(r'^pokemonTrainers/$',views.pokemonsTrainers),
# url(r'^trainers/$',views.trainers),
# url(r'^types/$',views.types)

def pokemons(request):
    pokemons = Pokemon.objects.all()
    serializer = PokemonSerializer(pokemons, many=True)
    return JsonResponse(serializer.data, safe = False, status=status.HTTP_200_OK)
