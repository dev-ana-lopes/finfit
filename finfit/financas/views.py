from django.http import JsonResponse
from financas.models import Usuario

def usuarios(request):
    if request.method == 'GET':
        usuario = {'id':1, 'nome': 'Guilherme'}

        return JsonResponse(usuario)


