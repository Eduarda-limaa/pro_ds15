from rest_framework import generics, parsers, status
from rest_framework.response import Response
import pandas as pd
from tablib import Dataset
from .resources import SensorResource

class ImportarSensores(generics.GenericAPIView):
    parser_classes= [parsers.MultiPartParser]

    def post(self, request, *args, **kwargs):
        file= request.FILES['sensores']
        df= pd.read_excel(file)

        dataset= Dataset().load(df.to_csv(index=False), format='csv')
        resource= SensorResource()
        result= resource.import_data(dataset, dry_run=True)

        if not result.has_errors():
            resource.import_data(dataset, dry_run=False)
            return Response({"status": "Importação realizada com sucesso!"})
        
        return Response({"status": "Erro ao importar!"}, status=status.HTTP_400_BAD_REQUEST)