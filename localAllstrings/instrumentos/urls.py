from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('Login',views.Login,name='Login'),
    path('Registrar',views.Registrar,name='Registrar'),
    path('Precios',views.Precios,name='Precios'),
    path('Compra',views.Compra,name='Compra'),
    path('Guitarras',views.Guitarras,name='Guitarras'),
    path('Bajos',views.Bajos,name='Bajos'),
    path('Formulario',views.Formulario,name='Formulario'),

]