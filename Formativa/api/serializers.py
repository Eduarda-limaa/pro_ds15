from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields= '__all__'

    def create(self, validated_data):
       usuario = Usuario.objects.create_user(
           username=validated_data['username'],
           categoria=validated_data['categoria'],
           ni=validated_data['ni'],
           telefone= validated_data['telefone'],
           password= validated_data['password']
       )
       return usuario

    def update(self, instance, validated_data):
        salvar_senha= validated_data.pop('password', None)

        for chave, valor in validated_data.items():
            setattr(instance, chave, valor)
        
        instance.set_password(salvar_senha)
        instance.save()
        return instance

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Disciplina
        fields= '__all__'

class ReservaAmbienteSerializer(serializers.ModelSerializer):
    class Meta:
        model= ReservaAmbiente
        fields= '__all__'

    def create(self, validated_data):
        reservas = ReservaAmbiente.objects.all()
        data_inicio = validated_data['data_inicio']
        data_termino = validated_data['data_termino']
        sala= validated_data['sala']
        if reservas.filter(data_inicio__lte = data_inicio, data_termino__gte= data_termino, sala = sala).exists():
            raise serializers.ValidationError("Essa sala já está reservada!")
        return super().create(validated_data)

class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data= super().validate(attrs)
        data['usuario'] = {
            'username': self.user.username,
            'categoria': self.user.categoria
        }
        return data
    

 