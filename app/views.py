from django.shortcuts import render
from app.models import *
# Create your views here.

def Display_Topics(request):
    QST=Topic.objects.all()
    d={'topics':QST}
    return render(request,'Display_Topics.html',d)


def Display_Webpage(request):
    QSW=Webpage.objects.all()
    d={'webpages':QSW}

    return render(request,'Display_Webpage.html',d)


def Display_Access(request):
    QSA=AccessRecords.objects.all()
    d={'access':QSA}
    return render(request,'Display_Access.html',d)
    