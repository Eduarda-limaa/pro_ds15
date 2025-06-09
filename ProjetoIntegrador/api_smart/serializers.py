from rest_framework import serializers
from .models import Sensores, Ambientes, Historico
import re


# Serializer responsável por validar os dados dos sensores antes de salvar
# Verifica se a unidade de medida está correta conforme o tipo de sensor
# Também valida se o endereço MAC está no formato XX:XX:XX:XX:XX:XX
class SensoresSerializer(serializers.ModelSerializer):
    class Meta:
        model= Sensores
        fields= '__all__'

    def validate(self, data):
       if(data['sensor'] == 'Temperatura' and data['unidade_med'] != '°C'):
           raise serializers.ValidationError('O sensor de temperatura não pode ser diferente de °C.')
       
       elif(data['sensor'] == 'Umidade' and data['unidade_med'] != '%'):
           raise serializers.ValidationError('O sensor de umidade não pode ser diferente de %.')
       
       elif(data['sensor'] == 'Luminosidade' and data['unidade_med'] != 'lux'):
           raise serializers.ValidationError('O sensor de luminosidade não pode ser diferente de lux.')
       
       elif(data['sensor'] == 'Contador' and data['unidade_med'] != 'uni'):
           raise serializers.ValidationError('O sensor de contagem não pode ser diferente de uni.')
       
       elif(data['sensor'] != 'Temperatura' and data['sensor'] != 'Umidade' and data['sensor'] != 'Luminosidade'  and data['sensor'] != 'Contador'):
            raise serializers.ValidationError('Não existe sensor diferente de  Temperatura, Umidade, Luminosidade e Contador! ')
       
       elif not(re.match (r"^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$",data.get('mac_address','') ) ):
            raise serializers.ValidationError('O endereço deve estar no formato correto XX:XX:XX:XX:XX:XX')

       return data
    
# Serializer responsável por validar os dados dos ambientes antes de salvar
class AmbientesSerializer(serializers.ModelSerializer):
    class Meta:
        model= Ambientes
        fields= '__all__'

# Serializer responsável por validar os dados do historico antes de salvar
class HistoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Historico
        fields= '__all__'