from django.shortcuts import render
from .AI import PromptGenerator
from datetime import date

today = date.today()
# Create your views here.

def Redactar(request):
        
    return render(request, "ReclamadorApp/index.html")
    


def Carta(request):
    if request.method == 'POST':
        remitente       =  request.POST.get('remitente')
        destinatario    =  request.POST.get('destinatario')
        contexto        =  request.POST.get('contexto')
        genero          =  request.POST.get('genero')
        emocion         =  request.POST.get('emocion')
        extension       =  request.POST.get('extension')
      
        carta = PromptGenerator(remitente, destinatario, contexto, genero, emocion, extension)
        fecha = today.strftime("%d/%m/%Y")
   
    return render(request, "ReclamadorApp/carta.html", {'carta': carta, 'fecha':fecha, 'remitente':remitente, 'destinatario':destinatario   })