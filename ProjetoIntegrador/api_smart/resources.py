from import_export import resources
from .models import Sensores, Ambientes, Historico

class SensorResource(resources.ModelResource):
    class Meta:
        model= Sensores


class AmbienteResource(resources.ModelResource):
    class Meta:
        model= Ambientes

class HistoricoResource(resources.ModelResource):
    class Meta:
        model= Historico