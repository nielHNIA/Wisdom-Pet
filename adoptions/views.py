from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Pet
# Create your views here.
def home(request):
    pets = Pet.objects.all()
    return render(request, 'adoptions/home.html', {'pets': pets})

def pet_detail(request, id):
    try:
        pet = Pet.objects.get(id=id)
    except Pet.DoesNotExist:
        raise HTTP404('Pet not found')
    return render(request,'adoptions/pet_detail.html',{'pet': pet})
