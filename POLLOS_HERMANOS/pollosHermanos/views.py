from django.shortcuts import render, redirect
from pollosHermanos.models import Reserva
from pollosHermanos.forms import FormReserva

# Create your views here.

def index(request):
    return render(request,"index.html")

def agragarReserva(request):
    form=FormReserva()
    if request.method=='POST':
        form=FormReserva(request.POST)
        if form.is_valid():
            form.save()
        return listarReserva(request)
    
    data={'form':form,"titulo":"Agrega una Reserva"}
    return render(request,"agregar.html",data)

def listarReserva(request):
    reserva=Reserva.objects.all()
    data={"reserva":reserva}
    return render(request,"reservas.html",data)
    
def eliminarReserva(request,id):
    reserva=Reserva.objects.get(id=id)
    reserva.delete()
    return redirect('/lista')

def actualizarReserva(request,id):
    reserva=Reserva.objects.get(id=id)
    form=FormReserva(instance=reserva)
    if request.method=='POST':
        form=FormReserva(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
        return redirect('/lista')
    data={'form':form,"titulo":"Actualizar Reserva"}
    return render(request,"agregar.html",data)