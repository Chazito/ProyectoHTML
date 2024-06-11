from django.shortcuts import render
from .models import Genero,Alumno

def index(request):
    alumnos = Alumno.objects.all()
    alumnos2 = Alumno.objects.raw("SELECT * FROM alumnos_alumno")
    context = {"alumnos":alumnos, "alumnos2":alumnos2}
    return render(request, 'alumnos/index.html', context)

def crud(request):
    alumnos = Alumno.objects.all()
    context = {'alumnos':alumnos}
    return render(request, 'alumnos/alumnos_list.html',context)

def alumnosAdd(request):
    print(request.method)
    if request.method != "POST":
        generos = Genero.objects.all()
        context = {'generos':generos}
        print("Not post")
        return render(request, 'alumnos/alumnos_add.html',context)
    else:
        print("post")
        rut=request.POST["rut"]
        nombre=request.POST["nombre"]
        aPaterno = request.POST["paterno"]
        aMaterno = request.POST["materno"]
        fechaNac = request.POST["fechaNac"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]

        objGenero = Genero.objects.get(id_genero = genero)
        objAlumno = Alumno.objects.create(rut=rut, nombre=nombre, apellido_paterno=aPaterno, apellido_materno=aMaterno, email=email, telefono=telefono, direccion=direccion, id_genero = objGenero, fecha_nacimiento = fechaNac, activo=1)
        objAlumno.save()
        context = {'mensaje':"Datos grabados correctamente."}
        return render(request, 'alumnos/alumnos_add.html',context)
    
def alumnos_del(request, pk):
    context = {}
    try:
        alumno = Alumno.objects.get(rut = pk)
        alumno.delete()
        mensaje="Datos eliminados correctamente"
        alumnos = Alumno.objects.all()
        context = {'alumnos':alumnos, 'mensaje':mensaje}
        return render(request, 'alumnos/alumnos_list.html',context)
    except:
        mensaje="Error. El rut no existe"
        alumnos = Alumno.objects.all()
        context = {'alumnos':alumnos, 'mensaje':mensaje}
        return render(request, 'alumnos/alumnos_list.html',context)

def alumnos_findEdit(request, pk):
    return