from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dc', views.test_api),
    path('echo', views.echo)
]