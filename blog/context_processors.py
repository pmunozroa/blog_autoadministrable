from .models import ConfiguracionBasica, Enlace, Categoria

def get_config(request):
    return {'configuracion': ConfiguracionBasica.objects.filter(activo=True).order_by('posicion').first()}

def get_rrss(request):
    return {'rrss':Enlace.objects.all()}

def get_cats(request):
    return {'categorias_listado':Categoria.objects.all()}