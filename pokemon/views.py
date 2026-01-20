from django.shortcuts import render, get_object_or_404
from .models import Pokemon
from django.http import HttpResponse, JsonResponse

# Create your views here.

# ENDPOINT: /pokemon/list
def pokemon_list(request):
    pokemon_queryset = Pokemon.objects.all()
    # Trasformiamo i dati in una lista di dizionari per il JSON
    data = list(pokemon_queryset.values("id", "name", "pokedex_id"))
    return JsonResponse(data, safe=False)

# ENDPOINT: /pokemon/delete/<id>/
def delete_pokemon(request, pk):
    # Cerchiamo il pokemon con quell'ID, se non esiste manda un errore 404
    pokemon_da_cancellare = get_object_or_404(Pokemon, pk=pk)
    
    nome_eliminato = pokemon_da_cancellare.name
    pokemon_da_cancellare.delete() # Ciao ciao Pokemon!
    
    return JsonResponse({"message": f"Il Pokemon {nome_eliminato} è stato liberato nel bosco!"})

def pokemon_list(request):
    # 1. Recupera tutti i pokemon dal DB (QuerySet)
    tutti_i_pokemon = Pokemon.objects.all()
    
    # 2. Crea una lista leggibile (per ora semplice testo)
    nomi = [p.name for p in tutti_i_pokemon]
    
    return HttpResponse(f"I tuoi Pokémon: {', '.join(nomi)}")

def add_pokemon(request):
    pokemon = Pokemon.objects.create(name="Bulbasaur", pokedex_id=1)
    return JsonResponse({'id': pokemon.id, 'name': pokemon.name, 'pokedex_id': pokemon.pokedex_id})