from django.shortcuts import render, redirect, get_object_or_404
from crudsimple.forms import FormFallecido ,FallecidoFilterForm
from crudsimple.models import Fallecido
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
from django.db.models import Count
from datetime import timedelta
from openpyxl import Workbook
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

@login_required
def listadoFallecidos(request):
    fallecidos = Fallecido.objects.all()  # Consulta base
    filter_form = FallecidoFilterForm(request.GET)  # Formulario para filtros

    # Aplicar filtros si el formulario es válido
    if filter_form.is_valid():
        rut = filter_form.cleaned_data.get('rut')
        nombre = filter_form.cleaned_data.get('nombre')
        apellido_p = filter_form.cleaned_data.get('apellido_p')
        apellido_m = filter_form.cleaned_data.get('apellido_m')
        fecha_inicio = filter_form.cleaned_data.get('fecha_inicio')
        fecha_fin = filter_form.cleaned_data.get('fecha_fin')
        ubicacion = filter_form.cleaned_data.get('ubicacion')

        # Filtros condicionales
        if rut:
            fallecidos = fallecidos.filter(rut__icontains=rut)
        if nombre:
            fallecidos = fallecidos.filter(nombre__icontains=nombre)
        if apellido_p:
            fallecidos = fallecidos.filter(apellido_p__icontains=apellido_p)
        if apellido_m:
            fallecidos = fallecidos.filter(apellido_m__icontains=apellido_m)
        if fecha_inicio and fecha_fin:
            fallecidos = fallecidos.filter(fechafallecimiento__range=(fecha_inicio, fecha_fin))
        elif fecha_inicio:
            fallecidos = fallecidos.filter(fechafallecimiento__gte=fecha_inicio)
        elif fecha_fin:
            fallecidos = fallecidos.filter(fechafallecimiento__lte=fecha_fin)
        if ubicacion:
            fallecidos = fallecidos.filter(ubicacion=ubicacion)

    context = {
        'fallecidos': fallecidos,
        'filter_form': filter_form,
    }
    return render(request, 'fallecidos.html', context)

@login_required
def agregarFallecido(request):
    if request.method == 'POST':
        form = FormFallecido(request.POST)
        rut = request.POST.get('rut')

        # Verificar si el RUT ya existe
        if Fallecido.objects.filter(rut=rut).exists():
            messages.error(request, "Este RUT ya está registrado.")
            return redirect('listadoFallecidos')

        if form.is_valid():
            form.save()
            messages.success(request, "Fallecido agregado exitosamente.")
            return redirect('listadoFallecidos')

    return redirect('listadoFallecidos')

@login_required
def actualizarFallecido(request, id):
    fallecido = get_object_or_404(Fallecido, id=id)

    if request.method == 'POST':
        form = FormFallecido(request.POST, instance=fallecido)
        if form.is_valid():
            form.save()
            messages.success(request, "Fallecido actualizado exitosamente.")
            return redirect('listadoFallecidos')
    else:
        form = FormFallecido(instance=fallecido)

    # Devuelve el formulario y la lista de fallecidos en caso de error
    fallecidos = Fallecido.objects.all()
    context = {'fallecidos': fallecidos, 'form': form, 'fallecido': fallecido}
    return render(request, 'fallecidos.html', context)

@login_required
def eliminarFallecido(request, id):
    fallecido = get_object_or_404(Fallecido, id=id)
    fallecido.delete()
    messages.success(request, "Fallecido eliminado exitosamente.")
    return redirect('listadoFallecidos')

def buscar_fallecido(request):
    nombre = request.GET.get('nombre', '').strip()
    apellido_p = request.GET.get('apellido_p', '').strip()
    apellido_m = request.GET.get('apellido_m', '').strip()
    rut = request.GET.get('rut', '').strip()

    if nombre and apellido_p and apellido_m:
        fallecidos = Fallecido.objects.filter(
            nombre=nombre,
            apellido_p=apellido_p,
            apellido_m=apellido_m
        )
    elif rut:
        fallecidos = Fallecido.objects.filter(rut=rut)
    else:
        fallecidos = Fallecido.objects.none()

    resultados = list(fallecidos.values())
    return JsonResponse({'resultados': resultados})

@login_required
def dashboard(request):
    total_fallecidos = Fallecido.objects.count()
    fallecidos_hoy = Fallecido.objects.filter(fechafallecimiento=timezone.now().date()).count()
    
    # Consulta para obtener la ubicación con más fallecidos
    ubicacion_mas_fallecidos = (
        Fallecido.objects.values('ubicacion')
        .annotate(total=Count('id'))
        .order_by('-total')
        .first()
    )
    
    # Consulta para obtener el número de fallecidos en la última semana
    una_semana_atras = timezone.now().date() - timedelta(days=7)
    fallecidos_ultima_semana = Fallecido.objects.filter(fechafallecimiento__gte=una_semana_atras).count()

    context = {
        'total_fallecidos': total_fallecidos,
        'fallecidos_hoy': fallecidos_hoy,
        'ubicacion_mas_fallecidos': ubicacion_mas_fallecidos,
        'fallecidos_ultima_semana': fallecidos_ultima_semana,
    }
    return render(request, 'dashboard.html', context)






def export_total_fallecidos(request):
    fallecidos = Fallecido.objects.all()
    return export_to_excel(fallecidos, 'Total Fallecidos')

def export_fallecidos_hoy(request):
    hoy = timezone.now().date()
    fallecidos = Fallecido.objects.filter(fechafallecimiento=hoy)
    return export_to_excel(fallecidos, 'Fallecidos Hoy')

def export_ubicacion_mas_fallecidos(request):
    # Ubicación con más fallecidos
    ubicacion_mas_fallecidos = (
        Fallecido.objects.values('ubicacion')
        .annotate(total=Count('id'))
        .order_by('-total')
        .first()
    )
    fallecidos = Fallecido.objects.filter(ubicacion=ubicacion_mas_fallecidos['ubicacion']) if ubicacion_mas_fallecidos else Fallecido.objects.none()
    return export_to_excel(fallecidos, 'Ubicación con Más Fallecidos')

def export_fallecidos_ultima_semana(request):
    una_semana_atras = timezone.now().date() - timedelta(days=7)
    fallecidos = Fallecido.objects.filter(fechafallecimiento__gte=una_semana_atras)
    return export_to_excel(fallecidos, 'Fallecidos Última Semana')

def export_to_excel(fallecidos, title):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{title}.xlsx"'

    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = title

    # Header
    headers = ['RUT', 'Nombre', 'Apellido P', 'Apellido M', 'Fecha Fallecimiento', 'Ubicación', 'Maps']
    worksheet.append(headers)

    # Data rows
    for fallecido in fallecidos:
        row = [
            fallecido.rut,
            fallecido.nombre,
            fallecido.apellido_p,
            fallecido.apellido_m,
            fallecido.fechafallecimiento,
            fallecido.ubicacion,
            fallecido.maps,
        ]
        worksheet.append(row)

    workbook.save(response)
    return response



def historias(request):
    return render(request, 'historias.html')


def sobrenosotros(request):
    return render(request, 'sobrenosotros.html')