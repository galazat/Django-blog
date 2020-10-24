from django.shortcuts import render

def notes(request):
    return render(request, 'static/templates/notes/notes.html', locals())