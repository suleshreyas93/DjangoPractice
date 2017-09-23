from django.shortcuts import render,get_object_or_404
#from django.http import HttpResponse
from . models import Albums
#from django.template import loader
from django.http import Http404

# Create your views here.
def index(request):
    all_albums = Albums.objects.all()
    #template = loader.get_template("music/index.html")
    context = {"all_albums" : all_albums}
    #return HttpResponse(template.render(context,request))
    return render(request,"music/index.html",context)
    

def details(request,album_id):
    
    # try:
    #     album = Albums.objects.get(pk = album_id)
    # except:
    #     raise Http404("Album does not exist")

    album = get_object_or_404(Albums,pk = album_id)
    return render(request,"music/details.html",{"album" : album})
