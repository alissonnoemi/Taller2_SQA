from django.urls import path
from .views import *

urlpatterns = [
    path("", pokemons, name="pokemons"),
    path("pokemons/<int:pokemon_id>/", pokemon_detail, name="pokemon_detail"),
    path("pokemons/create/", pokemon_create, name="pokemon_create"),
    path("pokemons/update/<int:pokemon_id>/", pokemon_update, name="pokemon_update"),
    path("pokemons/delete/<int:pokemon_id>/", pokemon_delete, name="pokemon_delete"),
]