from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("A senha deve ter pelo menos 8 caracteres.")
        if value.isdigit():
            raise serializers.ValidationError("A senha não pode conter apenas números.")
        return value

    def validate_ni(self, value):
        if not str(value).isdigit():
            raise serializers.ValidationError("O NI deve conter apenas números.")
        return value

    def create(self, validated_data):
        usuario = Usuario.objects.create_user(
            username=validated_data['username'],
            categoria=validated_data['categoria'],
            ni=validated_data['ni'],
            telefone=validated_data['telefone'],
            password=validated_data['password']
        )
        return usuario

    def update(self, instance, validated_data):
        salvar_senha = validated_data.pop('password', None)

        for chave, valor in validated_data.items():
            setattr(instance, chave, valor)

        if salvar_senha:
            instance.set_password(salvar_senha)

        instance.save()
        return instance

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Disciplina
        fields= '__all__'
    
    def validate_nome(self, value):
        if self.instance:
            if Disciplina.objects.filter(nome__iexact=value).exclude(pk=self.instance.pk).exists():
                raise serializers.ValidationError("Essa disciplina já está cadastrada.")
        else:
            if Disciplina.objects.filter(nome__iexact=value).exists():
                raise serializers.ValidationError("Essa disciplina já está cadastrada.")
        return value


class ReservaAmbienteSerializer(serializers.ModelSerializer):
    class Meta:
        model= ReservaAmbiente
        fields= '__all__'

    def create(self, validated_data):
        reservas = ReservaAmbiente.objects.all()
        data_inicio = validated_data['data_inicio']
        data_termino = validated_data['data_termino']
        periodo= validated_data['periodo']
        sala= validated_data['sala']

        if reservas.filter(data_inicio__lte = data_inicio, data_termino__gte= data_termino, sala = sala, periodo=periodo).exists() \
                    or reservas.filter(data_inicio__gte = data_inicio, data_termino__lte= data_termino, sala=sala, periodo=periodo).exists() \
                    or reservas.filter(data_inicio__lte = data_inicio, data_termino__lte= data_termino, data_termino__gte=data_inicio, sala=sala, periodo=periodo).exists() \
                    or reservas.filter(data_inicio__gte = data_inicio, data_termino__gte= data_termino, data_inicio__lte=data_termino, sala=sala, periodo=periodo).exists() :
           raise serializers.ValidationError({"data_inicio": "Essa sala já está reservada nesse período!"})
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        reservas = ReservaAmbiente.objects.exclude(pk=instance.pk)
        data_inicio = validated_data.get('data_inicio', instance.data_inicio)
        data_termino = validated_data.get('data_termino', instance.data_termino)
        periodo= validated_data['periodo']
        sala = validated_data.get('sala', instance.sala)

        if reservas.filter(data_inicio__lte=data_inicio, data_termino__gte=data_termino, sala=sala, periodo=periodo).exists() \
            or reservas.filter(data_inicio__gte=data_inicio, data_termino__lte=data_termino, sala=sala, periodo=periodo).exists() \
            or reservas.filter(data_inicio__lte=data_inicio, data_termino__lte=data_termino, data_termino__gte=data_inicio, sala=sala, periodo=periodo).exists() \
            or reservas.filter(data_inicio__gte=data_inicio, data_termino__gte=data_termino, data_inicio__lte=data_termino, sala=sala, periodo=periodo).exists():
            raise serializers.ValidationError({"data_inicio": "Essa sala já está reservada nesse período!"})

        return super().update(instance, validated_data)

class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data= super().validate(attrs)
        data['usuario'] = {
            'username': self.user.username,
            'categoria': self.user.categoria,
            'id' : self.user.id
        }
        return data
