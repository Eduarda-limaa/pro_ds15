from django.urls import path
from .import views

urlpatterns=[
    path('api-eventos/', views.read_eventos, name='read_eventos'),
    path('api-eventos/<int:pk>', views.read_evento, name='read_evento'),
    path('api-eventos/criar', views.create_evento, name='create_evento'),
    path('api-eventos/atualizar/<int:pk>', views.update_evento, name='update_evento'),
    path('api-eventos/deletar/<int:pk>', views.delete_evento, name='delete_evento'),
    path('api-eventos/proximos/', views.read_eventosproximos),
]