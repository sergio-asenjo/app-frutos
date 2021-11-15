from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Despacho
from .forms import BuscarForm, DespachoModelForm

# Create your views here.


def inicio_vista(request):
    return render(request, 'inicio.html', {})


def listar_pedidos_vista(request):
    listado = Despacho.objects.all()
    return render(request, 'listado_despachos.html', {'listado': listado})


def registro_despacho_vista(request):
    form = DespachoModelForm(request.POST or None)
    if form.is_valid():
        despacho = form.save()
        form = DespachoModelForm()
        return redirect('/registro_despacho_exitoso/')
    return render(request, 'registro_despacho.html', {'form': form})


def registro_despacho_exitoso_vista(request):
    return render(request, 'registro_despacho_exitoso.html', {})


def eliminar_despacho_vista(request):
    form = BuscarForm(request.POST or None)
    if form.is_valid():
        n_despacho = form.clean_n_despacho()
        despacho = Despacho.objects.get(numero_despacho=n_despacho)
        despacho.delete()
        return redirect('/eliminado_despacho_exitoso/')
    return render(request, 'eliminar_despacho.html', {'form': form})


def eliminar_despacho_exitoso_vista(request):
    return render(request, 'eliminar_despacho_exitoso.html', {})


def actualizar_despacho_vista(request):
    form = BuscarForm(request.POST or None)
    if form.is_valid():
        n_despacho = form.clean_n_despacho()
        despacho = Despacho.objects.get(numero_despacho=n_despacho)
        estado_despacho = request.POST.get("estado_despacho")
        despacho.estado_despacho = estado_despacho
        despacho.save()
        return redirect('/actualizado_exitoso/')
    return render(request, 'actualizar_despacho.html', {'form': form})


def actualizado_exitoso_vista(request):
    return render(request, 'actualizado_exitoso.html', {})
