from django.contrib import admin
from .models import *
from .forms import EnlaceForm, CategoriaExperienciaForm, ConfiguracionBasicaForm, CurriculumForm, PostForm

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'activo',)

admin.site.register(Categoria, CategoriaAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_creacion', 'activo')
    list_filter = ('categoria', 'fecha_creacion', 'activo')
    form = PostForm
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

admin.site.register(Post, PostAdmin)

class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'asunto', 'fecha_creacion', 'respondido')
    list_filter = ('fecha_creacion', 'respondido',)

admin.site.register(Contacto, ContactoAdmin)

class ConfiguracionBasicaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apodo', 'nombre_completo', 'run', 'email_contacto', 'numero_contacto', 'fecha_nacimiento', 'posicion', 'activo')
    form = ConfiguracionBasicaForm

admin.site.register(ConfiguracionBasica, ConfiguracionBasicaAdmin)

class EnlaceAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'link',  'size',  'grosor',  'activo', 'preview_icon', )
    form = EnlaceForm

    class Media:
        js = (
            '//unpkg.com/ionicons@5.0.0/dist/ionicons.js',
        )
admin.site.register(Enlace, EnlaceAdmin)

class CategoriaExperienciaAdmin(admin.ModelAdmin):
    list_display = ('tipo_experiencia',)
    form = CategoriaExperienciaForm

admin.site.register(CategoriaExperiencia, CategoriaExperienciaAdmin)

class CurriculumAdmin(admin.ModelAdmin):
    list_display = ('nombre_institucion', 'tipo_experiencia', 'nombre_cargo', 'fecha_inicio', 'fecha_termino', 'activo')
    form = CurriculumForm

admin.site.register(Curriculum, CurriculumAdmin)
admin.site.register(Banners)
