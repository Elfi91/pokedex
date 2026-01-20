from django.shortcuts import render, get_object_or_404
from .models import Pokemon
from django.http import HttpResponse, JsonResponse

# Create your views here.

# ENDPOINT: /pokemon/list
def pokemon_list(request):
    pokemon_queryset = Pokemon.objects.all()
    # Transform data into a list of dictionaries for JSON
    data = list(pokemon_queryset.values("id", "name", "pokedex_id"))
    return JsonResponse(data, safe=False)

# ENDPOINT: /pokemon/delete/<id>/
def delete_pokemon(request, pk):
    # Search for the pokemon with that ID, return 404 if it doesn't exist
    pokemon_to_delete = get_object_or_404(Pokemon, pk=pk)
    
    deleted_name = pokemon_to_delete.name
    pokemon_to_delete.delete() # Bye bye Pokemon!
    
    return JsonResponse({"message": f"Pokemon {deleted_name} was released into the wild!"})

def pokemon_list(request):
    # 1. Retrieve all pokemon from DB (QuerySet)
    all_pokemon = Pokemon.objects.all()
    
    # 2. Create a readable list (simple text for now)
    names = [p.name for p in all_pokemon]
    
    return HttpResponse(f"Your Pokemon: {', '.join(names)}")

def add_pokemon(request):
    pokemon = Pokemon.objects.create(name="Bulbasaur", pokedex_id=1)
    return JsonResponse({'id': pokemon.id, 'name': pokemon.name, 'pokedex_id': pokemon.pokedex_id})