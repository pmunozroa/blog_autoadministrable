from django.urls import path
from .views import HomeView, CategoriasView, ContactoView, PostsView, PostDetailView, CategoriasPostsView, CurriculumView, BannersView

blogpattern = ([
    path('', HomeView.as_view(), name="home"),
    path('categorias/', CategoriasView.as_view(), name="categorias"),
    path('categorias/<int:pk>/<slug:nombre>/', CategoriasView.as_view(), name="categorias"),
    path('posts/', PostsView.as_view(), name="posts" ),
    path('contacto/', ContactoView.as_view(), name="contacto"),
    path('post/<int:pk>/<slug:titulo>/', PostDetailView.as_view(), name="post"),
    path('contacto/success/', ContactoView.as_view(), name="contacto_success"),
    path('curriculum/', CurriculumView.as_view(), name="curriculum"),
    path('apoyame/', BannersView.as_view(), name="apoyo"),
], 'blog')