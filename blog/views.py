from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .models import *
from .forms import ContactoForm
from itertools import chain

class LoadPageConfig():
    def dispatch(self, request, *args, **kwargs):
        if ConfiguracionBasica.objects.filter(activo=True).order_by('posicion').first() is None:
            return redirect(reverse_lazy('admin:index'))
        return super().dispatch(request, *args, **kwargs)

class HomeView(LoadPageConfig, TemplateView):
    template_name = "blog/home.html"


class CategoriasView(LoadPageConfig, ListView):
    model = Post
    template_name = "blog/categorias.html"
    context_object_name = "posts"
    ordering = ['-fecha_creacion']
    paginate_by = 9

    def get_queryset(self):
        context = super().get_queryset()
        cat_pk = self.kwargs.get('pk', False)
        if cat_pk:
            return Post.objects.filter(categoria=cat_pk).order_by('-fecha_creacion')
        else:
            return context

class CategoriasPostsView(LoadPageConfig, ListView):
    model = Post
    template_name = "blog/categorias.html"
    context_object_name = "posts"
    ordering = ['-fecha_creacion']
    paginate_by = 9

    def get_queryset(self):
        context = super().get_queryset()
        cat_pk = self.kwargs.get('pk', False)
        if cat_pk != None:
            return Post.objects.filter(categoria=cat_pk).order_by('-fecha_creacion')

class PostsView(LoadPageConfig, ListView):
    model = Post
    template_name = "blog/posts.html"
    context_object_name = "posts"
    ordering = ['-fecha_creacion']
    paginate_by = 9

class ContactoView(SuccessMessageMixin, LoadPageConfig, CreateView):
    form_class = ContactoForm
    template_name = "blog/contacto.html"
    success_url = reverse_lazy('blog:contacto_success')
    success_message = "%(nombre)s, tu mensaje fue enviado correctamente, te contactaré pronto, gracias."


class PostDetailView(LoadPageConfig, DetailView):
    model = Post
    template_name = "blog/post.html"

class CurriculumView(LoadPageConfig, ListView):
    template_name = "blog/curriculum.html"
    model = CategoriaExperiencia
    context_object_name = "experiencias"

    def get(self, request, *args, **kwargs):
        cat_exp = CategoriaExperiencia.objects.all().count()
        exp_insc = Curriculum.objects.all().count()
        if cat_exp == 0 or exp_insc == 0:
            return redirect(reverse_lazy('blog:home'))
        return super().get(request, *args, **kwargs)

class BannersView(LoadPageConfig, ListView):
    template_name = "blog/banners.html"
    model = Banners
    context_object_name = "banners"

    def get_queryset(self):
          return Banners.objects.filter(activo=True)