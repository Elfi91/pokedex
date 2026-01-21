import json
from django.db import IntegrityError, OperationalError
from django.shortcuts import render, get_object_or_404
from .models import Pokemon
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST, require_GET
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
@require_POST
def add_pokemon(request):
    try:
        # Carica i dati JSON inviati nel corpo della richiesta
        data = json.loads(request.body)

        # Crea il nuovo record nel database usando i dati ricevuti
        pokemon = Pokemon.objects.create(
            name=data['name'],
            pokedex_id=data['pokedex_id']
        )

        # Restituisce i dati del Pokémon appena creato con status 201 (Created)
        return JsonResponse({
            'id': pokemon.id,
            'name': pokemon.name,
            'pokedex_id': pokemon.pokedex_id
        }, status=201)

    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON non valido'}, status=400)

    except KeyError as e:
        # Se manca uno dei campi obbligatori (name o pokedex_id)
        return JsonResponse({'error': f'Campo mancante: {e}'}, status=400)

    except (ValueError, TypeError):
        # Se i dati inviati non sono del tipo corretto
        return JsonResponse({'error': 'Tipo di dato non valido'}, status=400)

    except IntegrityError:
        # Se provi ad aggiungere un Pokémon che viola un vincolo di unicità
        return JsonResponse({'error': 'Pokemon già esistente'}, status=409)

    except OperationalError:
        return JsonResponse({'error': 'Database non disponibile'}, status=503)

    except Exception as e:
        return JsonResponse({'error': 'Errore interno del server'}, status=500)

@require_GET
def get_pokemon_list(request):
    try:
        pokemon_list = list(Pokemon.objects.all().values())
        return JsonResponse(pokemon_list, safe=False)

    except OperationalError:
        # Problemi di connessione al database
        return JsonResponse({'error': 'Database non disponibile'}, status=503)

    except Exception as e:
        # Errore generico imprevisto
        return JsonResponse({'error': str(e)}, status=500)


# ENDPOINT: /pokemon/delete/<id>/
def delete_pokemon(request, pk):
    # Search for the pokemon with that ID, return 404 if it doesn't exist
    pokemon_to_delete = get_object_or_404(Pokemon, pk=pk)
    
    deleted_name = pokemon_to_delete.name
    pokemon_to_delete.delete() # Bye bye Pokemon!
    
    return JsonResponse({"message": f"Pokemon {deleted_name} was released into the wild!"})