# Generated by Django 4.0 on 2022-12-16 16:13

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articulos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', tinymce.models.HTMLField()),
                ('estado', models.BooleanField(blank=True, default=True, null=True)),
                ('visibilidad', models.BooleanField(blank=True, default=False, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('titulo', models.CharField(max_length=255)),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articulos.articulo')),
            ],
            options={
                'db_table': 'comentarios',
            },
        ),
    ]
