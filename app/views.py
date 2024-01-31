from django.shortcuts import render

# Create your views here.
from app.models import *
from app.forms import *
from django.http import HttpResponse

def create_school(request):
    ESFO=Schoolform()
    d={'data':ESFO}
    
    if request.method=='POST':
        SFDO=Schoolform(request.POST)
        if SFDO.is_valid():
            sn=SFDO.cleaned_data['Sname']
            sp=SFDO.cleaned_data['Sprincipal']
            sl=SFDO.cleaned_data['Slocation']
            SO=School.objects.get_or_create(Sname=sn,Sprincipal=sp,Slocation=sl)[0]
            SO.save()
            return HttpResponse('School is created')
        else:
            return HttpResponse('Invalid data')

    return render(request,'create_school.html',d)