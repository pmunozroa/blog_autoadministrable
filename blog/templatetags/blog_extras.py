from django import template
from django.urls import reverse_lazy
from blog.models import Categoria, ConfiguracionBasica, Curriculum, Enlace, Post, CategoriaExperiencia
from django.db.models import Count

register = template.Library()


@register.simple_tag
def is_active(reverse, url):
    reversa = reverse_lazy(reverse)
    if url == reversa:
        return 'active'
    return ''

@register.simple_tag
def is_active_category(reverse, cat_id, cat_slug, url):
    reversa = reverse_lazy(reverse)
    param = f'{reversa}{cat_id}/{cat_slug}/'
    if url == param:
        return 'active'
    return ''

@register.simple_tag
def get_configuration():
    return ConfiguracionBasica.objects.filter(activo=True).order_by('posicion').first()

@register.simple_tag
def get_rrss():
    return Enlace.objects.all()

@register.simple_tag
def preview_posts():
    return Post.objects.all().order_by('-fecha_creacion')

@register.simple_tag
def get_cats():
    return Categoria.objects.all()

@register.filter
def get_cat_name(cat_id):
    categoria = Categoria.objects.filter(id=cat_id).first()
    if categoria is not None:
        return f' | {categoria.nombre}'
    return False

@register.simple_tag
def count_posts(cat_id):
    return Post.objects.filter(categoria=cat_id).count()

@register.simple_tag
def get_percentage(total_posts, post_cat):
    return ((100 / total_posts) * post_cat)

@register.simple_tag
def get_order_cat_by_total_posts():
    return Categoria.objects.annotate(posts=Count('post__id')).order_by('-posts')

@register.simple_tag
def any_experience():
    cat_exp = CategoriaExperiencia.objects.all().count()
    exp_insc = Curriculum.objects.all().count()
    if cat_exp == 0 or exp_insc == 0:
        return False
    return True

@register.simple_tag
def experiencie_type(type):
    if type == 'Laboral':
        return {'clase': 'work-experience', 'titulo': 'Experiencia Laboral'}
    elif type == 'Estudiantil':
        return {'clase': 'education', 'titulo': 'Educacion'}
    elif type == 'Curso':
        return {'clase': 'to-define', 'titulo': 'To Define'}
    elif type == 'Otras':
        return {'clase': 'to-define', 'titulo': 'To Define'}
    else:
        return 0

@register.simple_tag
def get_exp_by_cat(exp_cat_id):
    return Curriculum.objects.filter(tipo_experiencia=exp_cat_id, activo=True).order_by('-fecha_inicio').order_by('fecha_termino')