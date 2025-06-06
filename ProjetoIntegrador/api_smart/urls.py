from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,  TokenRefreshView
from .views import RetrieveUpdateDestroySensores, ListCreateSensores, ListCreateAmbientes, RetrieveUpdateDestroyAmbientes, ListCreateHistorico, RetrieveUpdateDestroyHistorico, ExportarSensor, ExportarAmbiente, ExportarHistorico
from .importe import ImportarSensores

urlpatterns= [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('sensores/', view=ListCreateSensores.as_view(), name='criacao_sensores'),
    path('sensores/<int:pk>', view=RetrieveUpdateDestroySensores.as_view(), name='detalhes_sensores'),
    path('ambiente/', view=ListCreateAmbientes.as_view(), name='criacao_ambiente'),
    path('ambiente/<int:pk>', view=RetrieveUpdateDestroyAmbientes.as_view(), name='detalhes_ambientes'),
    path('historico/', view=ListCreateHistorico.as_view(), name='criacao_historico'),
    path('historico/<int:pk>', view=RetrieveUpdateDestroyHistorico.as_view(), name='detalhes_historico'),
    path('importar/', view=ImportarSensores.as_view(), name='importa arquivos'),
    path('exportar/sensor/', view=ExportarSensor.as_view(), name='exportar sensores'),
    path('exportar/ambiente/', view=ExportarAmbiente.as_view(), name='exportar ambiente'),
    path('exportar/historico/', view=ExportarHistorico.as_view(), name='exportar historico'),
]

