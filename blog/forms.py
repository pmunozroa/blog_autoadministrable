from django.forms import ModelForm
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Contacto, Enlace, CategoriaExperiencia, ConfiguracionBasica, Curriculum, Post

tipo = (
    ("logo-facebook", "Facebook"),
    ("logo-instagram", "Instagram"),
    ("logo-twitter", "Twitter"),
    ("logo-pinterest", "Pinterest"),
    ("logo-reddit", "Reddit"),
    ("logo-youtube", "Youtube"),
)

size = (
    ("small", "Pequeño"),
    (" ", "Normal"),
    ("large", "Grande"),
)

grosor = (
    ("thin", "Fino"),
    (" ", "Normal"),
    ("bold", "Grueso"),
)

tipo_experiencia = (
    ("Laboral", 'Laboral'),
    ('Estudiantil', 'Estudiantil'),
    ('Curso', 'Curso'),
    ('Otras', 'Otras'),
)


class ContactoForm(ModelForm):
    """ContactoForm definition."""
    class Meta:
        model = Contacto
        fields = ('__all__')
        exclude = ('respondido', )

    def __init__(self, *args, **kwargs):
        super(ContactoForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({'autofocus': ''})

    nombre = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'nombre_contacto'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'id': 'email_contacto'}))
    asunto = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'asunto_contacto'}))
    mensaje = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'id': 'mensaje__contacto'}))
    # TODO: Define form fields here


class EnlaceForm(ModelForm):
    """EnlaceForm definition."""
    class Meta:
        model = Enlace
        fields = ('__all__')

    tipo = forms.ChoiceField(choices=tipo)
    link = forms.URLField()
    size = forms.ChoiceField(choices=size)
    grosor = forms.ChoiceField(choices=grosor)
    # TODO: Define form fields here

class CategoriaExperienciaForm(ModelForm):
    """EnlaceForm definition."""
    class Meta:
        model = CategoriaExperiencia
        fields = ('__all__')

    tipo_experiencia = forms.ChoiceField(choices=tipo_experiencia)
    # TODO: Define form fields here

class ConfiguracionBasicaForm(ModelForm):
    class Meta:
        model = ConfiguracionBasica
        fields = ('__all__')

    descripcion_corta = forms.CharField(widget=CKEditorWidget())
    descripcion_general = forms.CharField(widget=CKEditorWidget())

class CurriculumForm(ModelForm):
    class Meta:
        model = Curriculum
        fields = ('__all__')

    descripcion = forms.CharField(widget=CKEditorWidget())

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('__all__')

    descripcion = forms.CharField(widget=CKEditorWidget())