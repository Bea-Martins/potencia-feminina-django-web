from django.shortcuts import render
from django.http import HttpResponse

# Cada view redireciona pra uma página, arquivo html, informação
def inicio(request):
  return render(request, 'inicio.html')

def cadastro(request):
  return render(request, 'cadastro.html')