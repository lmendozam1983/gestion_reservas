from django.shortcuts import render, redirect, get_object_or_404
from .models import SalaModel, ReservaModel
from .forms import SalaForm, ReservaForm
# Create your views here.

def lista_salas(request):
    salas = SalaModel.objects.all()
    return render(request,'lista_salas.html', {'salas': salas})

def detalle_sala(request, pk):
    sala = get_object_or_404(SalaModel, pk=pk)
    return render(request, 'detalle_salas.html', {'sala': sala})


def agregar_salas(request):
    if request.method == 'POST':
        form = SalaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_salas')
    else:
        form = SalaForm()
    return render(request, 'agregar_salas.html', {'form': form})

def editar_sala(request,pk):

    sala = get_object_or_404(SalaModel, pk=pk)
    if request.method == 'POST':
        form = SalaForm(request.POST, instance=sala)
        if form.is_valid():
            form.save()
            return redirect('/salas')
    else:
        form = SalaForm(instance=sala)
        context = {'form': form}
    return render(request, 'editar_salas.html',context)

def eliminar_sala(request, pk):
    sala = get_object_or_404(SalaModel, pk=pk)
    sala.delete()
    return redirect('lista_salas')

def lista_reservas(request):
    reservas = ReservaModel.objects.all()
    context = {'reservas': reservas}
    return render(request, 'lista_reservas.html',context)

def agregar_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirige después de guardar para evitar reenvíos
            return redirect('reservas')  # Reemplaza con la URL name correcta
        else:
            # Si el formulario no es válido, renderiza con los errores
            return render(request, 'agregar_reserva.html', {'form': form})
    else:
        form = ReservaForm()
        return render(request, 'agregar_reserva.html', {'form': form})

def editar_reserva(request,pk):
    reserva = get_object_or_404(ReservaModel, pk=pk)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('reservas')
    else:
        form = ReservaForm(instance=reserva)
        context = {'form': form}
    return render(request, 'editar_reserva.html',context)

def eliminar_reserva(request, reserva_pk):
    reserva = get_object_or_404(ReservaModel, pk=reserva_pk)
    reserva.delete()
    return redirect('reservas')
