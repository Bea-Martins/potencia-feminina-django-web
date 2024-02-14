from django.shortcuts import render

# Cada view redireciona pra uma página, arquivo html, informação
def inicio(request):
  return HttpResponse('Olá mundo!')

def cadastro(request):
  pass