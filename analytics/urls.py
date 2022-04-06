from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('health', views.health, name='index'),
    path('uploadfile', views.uploadfile, name='uploadfile'),
    path('predic_cifar', views.predict_cifar, name='predict_cifar'),
    path('predict_mnist', views.predict_mnist, name='predict_mnist'),
]