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
    url(r'^pokemons/$', views.pokemons)
    # url(r'^pokemonTrainers/$', views.pokemonsTrainers),
    # url(r'^trainers/$', views.trainers),
    # url(r'^types/$', views.types)



    # url(r'^professors/([0-9]{4})/$', views.professorDetails),
    # url(r'^promotions/$', views.promotions),
    # url(r'^promotions/([0-9]{4})/$', views.promotionDetails),
    # url(r'^students/$', views.students),
    # url(r'^students/([0-9]{4})/$', views.studentDetails),
    # url(r'^subjects/$', views.subjects),
    # url(r'^subjects/([0-9]{4})/$', views.subjectDetails),
    # url(r'^classes/$', views.classes),
    # url(r'^classes/([0-9]{4})/$', views.classeDetails)
]