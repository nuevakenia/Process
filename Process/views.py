from django.shortcuts import render

def inicio(request):
    
    return render(request, "inicio.html")

def tablero(request):
    
    return render(request, "tablero.html")

    
def barmenu(request):

    return render(request, "barmenu.html")    