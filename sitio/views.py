from django.shortcuts import render

from .models import Membro, Servicos


def index(request):
	template_name = 'sitio/index.html'
	equipe = Membro.objects.all()
	services = Servicos.objects.all()
	context = {
		'membros': equipe,
		'services': services,
	}

	return render(request, template_name, context)