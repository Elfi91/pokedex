from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.add_pokemon, name="add_pokemon"), # GET
    path("list/", views.pokemon_list, name="pokemon_list"),
    # The "trick": capture the UUID in the URL
    path("delete/<str:pk>/", views.delete_pokemon, name="delete_pokemon"),
]