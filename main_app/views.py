from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pokemon
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
    training_form = TrainingForm()
    return render(request, 'pokemon/detail.html', {
        'pokemon': pokemon,
        'training_form': training_form
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
    fields = '__all__'


class PokemonUpdate(UpdateView):
    model = Pokemon
    fields = ['level', 'description']


class PokemonDelete(DeleteView):
    model = Pokemon
    success_url = '/pokemon/'
