from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Pokemon, Item
from .forms import TrainingForm

# Define the home view


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def pokemon_index(request):
    pokemon = Pokemon.objects.all()
    return render(request, 'pokemon/index.html', {'pokemon': pokemon})


def pokemon_detail(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    items_pokemon_doesnt_have = Item.objects.exclude(id__in=pokemon.items.all().values_list('id'))
    training_form = TrainingForm()
    return render(request, 'pokemon/detail.html', {
        'pokemon': pokemon,
        'training_form': training_form,
        'items': items_pokemon_doesnt_have
    })

def add_training(request, pokemon_id):
    form = TrainingForm(request.POST)
    if form.is_valid():
        new_training = form.save(commit=False)
        new_training.pokemon_id = pokemon_id
        new_training.save()
    return redirect('detail', pokemon_id=pokemon_id)


class PokemonCreate(CreateView):
    model = Pokemon
    fields = ['name', 'level', 'element', 'description']


class PokemonUpdate(UpdateView):
    model = Pokemon
    fields = ['level', 'description']


class PokemonDelete(DeleteView):
    model = Pokemon
    success_url = '/pokemon/'

class ItemList(ListView):
  model = Item

class ItemDetail(DetailView):
  model = Item

class ItemCreate(CreateView):
  model = Item
  fields = '__all__'

class ItemUpdate(UpdateView):
  model = Item
  fields = ['name', 'effect']

class ItemDelete(DeleteView):
  model = Item
  success_url = '/items/'

def assoc_item(request, pokemon_id, item_id):
  Pokemon.objects.get(id=pokemon_id).items.add(item_id)
  return redirect('detail', pokemon_id=pokemon_id)

# def unassoc_item(request, pokemon_id, item_id):
#   Pokemon.objects.get(id=pokemon_id).items.remove(item_id)
#   return redirect('detail', pokemon_id=pokemon_id)