from django.shortcuts import render, get_object_or_404, redirect
from .models import Pokemon
from .forms import PokemonForm


# Create your views here.

def pokemons(request):
    pokemons = Pokemon.objects.all()
    return render(request, 'pokemons/pokemons.html', {'pokemons': pokemons})

def pokemon_detail(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    return render(request, 'pokemons/pokemon_detail.html', {'pokemon': pokemon})

def pokemon_create(request):
    if request.method == "POST":
        form = PokemonForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'pokemons/pokemon_detail.html', {'pokemon': form.instance})
    else:
        form = PokemonForm()
    return render(request, 'pokemons/pokemon_form.html', {'form': form})

def pokemon_update(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)

    if request.method == "POST":
        form = PokemonForm(request.POST, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('pokemon_detail', pokemon_id=pokemon.id)
    else:
        form = PokemonForm(instance=pokemon)

    return render(request, 'pokemons/pokemon_form.html', {'form': form})

def pokemon_delete(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    pokemon.delete()
    return redirect('pokemons')
    