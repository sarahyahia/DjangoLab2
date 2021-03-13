from django.shortcuts import render , redirect
from .forms import MovieForm,CategoryForm
from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    return render(request, "netflix/index.html", {
        'movies':movies
    })



def create(request):
    form = MovieForm(request.POST or None , request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("index")

    return render(request, "netflix/create.html", {
        'form':form
    })


def display(request,id):
    movie = Movie.objects.get(pk = id)
    return render(request, f"netflix/display.html", {
        "movie":movie
    })


def update(request,id):
    movie = Movie.objects.get(pk = id)
    form = MovieForm(request.POST or None , request.FILES or None , instance=movie)
    if form.is_valid():
        form.save()
        return render(request, "netflix/display.html",{
            "movie":movie
        })

    return render(request, "netflix/update.html", {
        'form':form,
        'movie':movie
    })

def delete(request,id):
    movie = Movie.objects.get(pk = id)
    movie.delete()
    return redirect("index")