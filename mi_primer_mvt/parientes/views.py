from django.shortcuts import render
from parientes.models import Parientes

def create_datos_familiares(request):
    new_parent = Parientes.objects.create(name = 'Silvana', last_name = 'Romano', age = 54, tipo_de_parentezco = 'Madre')
    context = {
        'new_parent': new_parent
    }
    return render(request, 'new_parent.html', context=context)

def list_parientes(request):
    parientes = Parientes.objects.all()
    context = {
        'parientes':parientes
    }
    return render(request, 'parents_list.html', context=context)