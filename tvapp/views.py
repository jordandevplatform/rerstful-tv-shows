
from django.shortcuts import render, redirect
from .models import Shows
from django.contrib import messages

def index(request):
    # if ("title" not in request.session):
        # return render(request, 'tvshows.html')
    
    # context = {
        # "allshows" : Shows.objects.all()
    # }
    return render(request, 'tvshows.html')

def shows (request):
    context = {
        'shows' : Shows.objects.all()
    }
    return render (request, 'shows.html', context)

def showid (request, theId):
    context = {
        'displayshow' : Shows.objects.get(id=theId)
    }
    return render (request, 'displayshow.html', context)
# def one_show(request, id):
#     context = {
#         'one_show' : Shows.objects.get(id=id)
#     }
# def new(request):
#     return render(request, 'addnewshow.html')

def editShow(request, theId):
    context = {
        'the_show' : Shows.objects.get(id=theId)
    }
    return render(request, 'editshow.html', context)

def update(request, theId):

    errors = Shows.objects.basic_validator(request.POST)
    
    if len(errors) > 0:
        
        for key, value in errors.items():
            messages.error(request, value)
            
            return redirect ('/shows/edit'+id)
        else: 
            
            show = Shows.objects.get(id=theId)
            show.title = request.POST['title']
            show.network = request.POST['network']
            show.date = request.POST['date']
            show.description = request.POST['description']
            show.save()
            messages.success(request, "Show succesfully updated")
            
            return redirect ('/shows')
    this_show = Shows.objects.get(id=theId)
    this_show.title = request.POST['title']
    this_show.network = request.POST['network']
    this_show.date = request.POST['date']
    this_show.description = request.POST['description']
    this_show.save()
    return redirect(f'/shows/{this_show.id}')

def deleteshow(request, theId):
    show = Shows.objects.get(id=theId)
    if (request.method == "GET"):
        show.delete()
    return redirect ('/shows')

def create(request):
    
    # errors = Shows.objects.basic_validator(request.POST)

    # if len(errors) > 0:
    #     for k, v in errors.items():
    #         messages.error(request, v)
    #     return redirect('/shows')

    title = request.POST['title']
    network = request.POST['network']
    release_date = request.POST['date']
    desc = request.POST['description']
    
    show = Shows.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        date = request.POST['date'],
        description = request.POST['description']
    )
    return redirect(f'/shows/{show.id}')