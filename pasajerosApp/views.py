from django.shortcuts import render, redirect
from pasajerosApp.forms import FormPasajero
from pasajerosApp.models import Pasajero

# Create your views here.
def index(request):
    return render(request, 'index.html')

def listadoPasajeros(request):
    pasajeros = Pasajero.objects.all()
    data = {'pasajeros' : pasajeros}
    return render(request, 'pasajeros.html', data)

def agregarPasajero(request):
    form = FormPasajero()
    if request.method == 'POST':
        form = FormPasajero(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/pasajeros')
    data = {'form' : form}
    return render(request, 'agregarPasajero.html', data)

def eliminarPasajero(request, id):
    pasajero = Pasajero.objects.get(id = id)
    pasajero.delete()
    return redirect('/pasajeros')

def actualizarPasajero(request, id):
    pasajero = Pasajero.objects.get(id = id)
    form = FormPasajero(instance=pasajero)
    if request.method == 'POST':
        form = FormPasajero(request.POST, instance=pasajero)
        if form.is_valid():
            form.save()
        return redirect('/pasajeros')
    data = {'form' : form}
    return render(request, 'agregarPasajero.html', data)