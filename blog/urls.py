from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.blog, name='Blog'),
    path('crearPost', views.create_post, name='CrearPost'),
    path('post', views.read_post, name='Post'),
    path('delete_post', views.delete_post, name='Delete'),
    path('edit', views.edit_post, name='EditPost'),
    path('comentar', views.CreateComment, name='Comentar'),
    path('delete_comment', views.DeleteComment, name='DeleteComment'),
]
