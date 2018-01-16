# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_list_or_404,get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework import  status
from .models import Pokemon
from django.views.decorators.csrf import csrf_exempt
from pokeDjangoRestApi.serializers import *

from django.shortcuts import render

# Create your views here.
# url(r'^pokemons/$',views.pokemons),
# url(r'^pokemonTrainers/$',views.pokemonsTrainers),
# url(r'^trainers/$',views.trainers),
# url(r'^types/$',views.types)

@csrf_exempt
def pokemons(request):
    print(request.method )
    if request.method == 'GET':
        pokemons = Pokemon.objects.all()
        serializer = PokemonSerializer(pokemons, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        #print(request.)
        #pokemon = request.POST.get('pokemon')
        #pokemon.save()
        return HttpResponse(status=status.HTTP_200_OK)


