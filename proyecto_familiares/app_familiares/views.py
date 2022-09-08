from django.http import HttpResponse
from django.template import Template, Context, loader
from app_familiares.models import Familiar

def ver_familiares (request):
    queryset = Familiar.objects.all()
    diccionario = {'familiares':queryset}
    plantilla = loader.get_template('template_familiares.html')
    documento_html = plantilla.render(diccionario)

    return HttpResponse (documento_html)

