from django.shortcuts import render

def estudiante(request):
    return render(request,'estudiantes/estudiante_form.html')

