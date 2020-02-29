from django.urls import path
from .views import HomeView, CategoriasView, ContactoView, PostsView, PostDetailView, CurriculumView, BannersView, request_filter_posts

blogpattern = ([
    path('', HomeView.as_view(), name="home"),
    path('categorias/', CategoriasView.as_view(), name="categorias"),
    path('categorias/<int:pk>/<slug:nombre>/', CategoriasView.as_view(), name="categorias"),
    path('contacto/', ContactoView.as_view(), name="contacto"),
    path('contacto/success/', ContactoView.as_view(), name="contacto_success"),
    path('posts/view/<int:pk>/<slug:titulo>/', PostDetailView.as_view(), name="post_view"),
    path('posts/filter/<slug:q>/', PostsView.as_view(), name="posts"),
    path('posts/', PostsView.as_view(), name="posts" ),
    path('curriculum/', CurriculumView.as_view(), name="curriculum"),
    path('apoyame/', BannersView.as_view(), name="apoyo"),
    path('posts/ajax/filter/', request_filter_posts, name="post_filter")
], 'blog')