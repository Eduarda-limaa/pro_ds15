from rest_framework import generics, parsers,status
from rest_framework.response import Response
import pandas as pd
from tablib import Dataset
from .resources import SensorResource, AmbienteResource, HistoricoResource

# Arquivo responsável por importar dados de sensores, ambientes e histórico a partir de arquivos Excel 
# Esses arquivos são processados e convertidos para um formato compatível com o Import-Export
# Os dados são importados usando seus resources (SensorResource, AmbienteResource, HistoricoResource)
# No caso de erro durante a importação, uma mensagem é retornada com os detalhes

class ImportarSensores(generics.GenericAPIView):
    parser_classes= [parsers.MultiPartParser]

    def post(self, request, *args, **kwargs):
        fileSensores = request.FILES['sensores']
        fileAmbientes= request.FILES['ambientes']
        fileHistorico= request.FILES['historico']

        try:
            importar(SensorResource(), fileSensores)
            importar(AmbienteResource(), fileAmbientes)
            importar(HistoricoResource(), fileHistorico)
            return Response("status:" "importação realizada com sucesso!")
        except ValueError as e:
            return Response(f"Erro ao importar!{e}", status=status.HTTP_400_BAD_REQUEST)
    
def importar(resource, file):
    df= pd.read_excel(file)
    
    dataset= Dataset().load(df.to_csv(index=False), format='csv')
    
    result= resource.import_data(dataset, dry_run=False)

    if not result.has_errors():
        return Response({"status": "Importação realizada com sucesso!"})
    raise ValueError( f"{file}  - {result.row_errors()}")