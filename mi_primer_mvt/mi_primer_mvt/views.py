from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def saludo(request):
    return HttpResponse('Holis Segunda clase con django')

def segundo_template(request):
    today = datetime.now().date
    context = {
        'name':'Maximiliano',
        'last_name':'Cantero',
        'today': today
    }
    return render(request, 'template_2.html', context=context)

def template_con_lista(request):
    context ={
        'family':['Silvana Romano','Ricardo Cantero','Alan Cantero','Belen cantero'],
    }
    return render(request, 'template_lista.html', context=context)