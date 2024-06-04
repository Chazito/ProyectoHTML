from django.shortcuts import render
from .models import Genero,Alumno

def index(request):
    alumnos = Alumno.objects.all()
    alumnos2 = Alumno.objects.raw("SELECT * FROM alumnos_alumno")
    context = {"alumnos":alumnos, "alumnos2":alumnos2}
    return render(request, 'alumnos/index.html', context)