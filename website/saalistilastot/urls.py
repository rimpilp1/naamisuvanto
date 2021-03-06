from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post', views.post, name='post'),
    path('tilastot', views.table, name='table'),
    path('suurin', views.biggest, name='table'),
    path('parse', views.parse, name='parse'),
    path('delete', views.delete, name='delete'),
]
