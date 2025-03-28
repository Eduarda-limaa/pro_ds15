from django.urls import path
from . import views

urlpatterns=[
    path('criar/', view=views.registrar, name='registrar'),
    path('logar/', view=views.logar, name='logar'),
    path('teste/', view=views.view_protegida, name='view protegida'),
]