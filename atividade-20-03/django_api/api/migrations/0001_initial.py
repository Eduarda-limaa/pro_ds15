# Generated by Django 5.1.7 on 2025-03-20 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('descriacao', models.TextField()),
                ('data_hora', models.DateTimeField()),
                ('local', models.CharField(blank=True, max_length=40)),
                ('categoria', models.TextField(blank=True)),
            ],
        ),
    ]
