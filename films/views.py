from django.shortcuts import render

def bestFilm(request):
    return render(request, 'static/templates/films/films.html', locals())
