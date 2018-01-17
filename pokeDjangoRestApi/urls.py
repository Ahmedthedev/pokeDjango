"""pokeDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^pokemons/$', views.pokemons),
    url(r'^pokemons/(?P<pokemon_id>[0-9]+)/$', views.pokemonsById),
    url(r'^pokemonTrainers/$', views.pokemonsTrainers),
    url(r'^pokemonTrainers/(?P<pokemonsTrainers_id>[0-9]+)/$', views.pokemonsTrainersById),
    url(r'^trainers/$', views.trainers),
    url(r'^trainers/(?P<trainers_id>[0-9]+)/$', views.trainersById),
    url(r'^types/$', views.types),
    url(r'^types/(?P<types_id>[0-9]+)/$', views.typesById),
    url(r'^images/$', views.imgs),
]