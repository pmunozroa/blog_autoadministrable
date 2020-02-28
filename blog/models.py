from django.db import models
from django.utils.html import format_html
from django.templatetags.static import static
from taggit.managers import TaggableManager


# Create your models here.
class Categoria(models.Model):

    nombre = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Categoria Post'
        verbose_name_plural = 'Categorias Posts'

class Post(models.Model):

    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to="posts/")
    activo = models.BooleanField(default=True)
    tags = TaggableManager()

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

class Contacto(models.Model):

    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    asunto = models.CharField(max_length=50)
    mensaje = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    respondido = models.BooleanField(default=False)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Mensaje'
        verbose_name_plural = 'Mensajes'

class ConfiguracionBasica(models.Model):

    posicion = models.IntegerField(default=0, unique=True, help_text="La posicion 0 será la que se utilizará en la página")
    banner = models.ImageField(upload_to="page/")
    avatar = models.ImageField(upload_to="page/")
    nombre = models.CharField(max_length=50)
    apodo = models.CharField(max_length=50)
    descripcion_corta = models.CharField(max_length=100)
    descripcion_general = models.CharField(max_length=250)
    nombre_completo = models.CharField(max_length=250)
    run = models.CharField(max_length=12, help_text="Formato sugerido XX.XXX.XXX-X, no está validado, así que depende de tí")
    email_contacto = models.EmailField()
    numero_contacto = models.CharField(max_length=8, help_text="No añadir el +569")
    fecha_nacimiento = models.DateField()
    hobbies = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    share_this = models.URLField(blank=True, null=True, help_text="https://sharethis.com/onboarding/")

    class Meta:
        verbose_name = 'Configuración Básica'
        verbose_name_plural = 'Configuraciones Básicas'

    def __str__(self):
        return self.apodo

class Enlace(models.Model):

    tipo = models.CharField(max_length=50, unique=True)
    link = models.URLField(help_text="Poner ruta completa, ejemplo https://www.facebook.com/<username>/")
    icons_folder = models.TextField(default=static('blog/ionicons'), editable=False)
    size = models.CharField(max_length=50)
    grosor = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)

    def preview_icon(self):
        return format_html(f'<ion-icon src="{self.icons_folder}/{self.tipo}.svg" size="{self.size}" class="{self.grosor}"></ion-icon>')
    preview_icon.allow_tags = True

    def __str__(self):
        return self.tipo

    class Meta:
        verbose_name = 'Redes Sociales'
        verbose_name_plural = 'Redes Sociales'

class CategoriaExperiencia(models.Model):
    """Model definition for CategoriaExperiencia."""

    tipo_experiencia = models.CharField(max_length=50, unique=True)

    class Meta:
        """Meta definition for CategoriaExperiencia."""

        verbose_name = 'Categoria Curriculum'
        verbose_name_plural = 'Categorias Curriculum'

    def __str__(self):
        """Unicode representation of CategoriaExperiencia."""
        return self.tipo_experiencia


class Curriculum(models.Model):
    tipo_experiencia = models.ForeignKey(CategoriaExperiencia, on_delete=models.DO_NOTHING)
    nombre_institucion = models.CharField(max_length=50)
    nombre_cargo = models.CharField(max_length=50, help_text="Cargo, Carrera, Curso o Tipo de enseñanza")
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField(blank=True, null=True, help_text="Dejar en blanco si aún estás trabajando")
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    activo = models.BooleanField(default=True, verbose_name="Mostrar?")

    def __str__(self):
        return self.nombre_institucion

    class Meta:
        verbose_name = 'Experiencia Curriculum'
        verbose_name_plural = 'Experiencias Curriculum'

class Banners(models.Model):

    imagen_banner = models.ImageField(upload_to="banners/")
    link = models.URLField(help_text="Link al portal de donación")
    titulo = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Banners'
        verbose_name_plural = 'Banners'