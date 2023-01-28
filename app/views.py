from django.shortcuts import render
from app.models import *
# Create your views here.
from django.db.models.functions import Length
from django.db.models import Q
    

def Display_Topics(request):
    QST=Topic.objects.all()
    d={'topics':QST}
    return render(request,'Display_Topics.html',d)


def Display_Webpage(request):
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(name__startswith='b')
    QSW=Webpage.objects.filter(name='revi')
    QSW=Webpage.objects.exclude(topic_name='Cricket')
    QSW=Webpage.objects.all()[:2:]
    QSW=Webpage.objects.all().order_by('name')
    QSW=Webpage.objects.all().order_by('-name')
    QSW=Webpage.objects.all().order_by(Length('name').desc())
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(url__endswith='com')
    QSW=Webpage.objects.filter(name__contains='b')
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(name__regex='\w{2}')
    QSW=Webpage.objects.filter(name__in=['binod','virat'])
    QSW=Webpage.objects.filter(Q(topic_name='Cricket') | Q(name='binod'))
    QSW=Webpage.objects.filter(Q(topic_name='VollyBall') & Q(url__startswith='https'))


    d={'webpages':QSW}

    return render(request,'Display_Webpage.html',d)


def Display_Access(request):
    QSA=AccessRecords.objects.all().order_by('date')
    QSA=AccessRecords.objects.all()
    QSA=AccessRecords.objects.filter(date='2023-01-10')
    QSA=AccessRecords.objects.filter(date__gt='2023-01-10')
    QSA=AccessRecords.objects.filter(date__gte='2023-01-10')
    QSA=AccessRecords.objects.filter(date__lt='2023-01-10')
    QSA=AccessRecords.objects.filter(date__lte='2023-01-10')
    QSA=AccessRecords.objects.all()
    QSA=AccessRecords.objects.filter(date__year='2023')
    QSA=AccessRecords.objects.filter(date__month='9')
    QSA=AccessRecords.objects.filter(date__day='24')
    QSA=AccessRecords.objects.all()
    QSA=AccessRecords.objects.filter(date__year__gt='2022')
    



    d={'access':QSA}
    return render(request,'Display_Access.html',d)
    