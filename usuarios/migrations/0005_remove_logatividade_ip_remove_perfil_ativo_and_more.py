# Generated by Django 5.2 on 2025-05-13 01:01

import datetime

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("usuarios", "0004_logatividade"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="logatividade",
            name="ip",
        ),
        migrations.RemoveField(
            model_name="perfil",
            name="ativo",
        ),
        migrations.RemoveField(
            model_name="perfil",
            name="data_nascimento",
        ),
        migrations.AddField(
            model_name="perfil",
            name="cpf",
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
        migrations.AddField(
            model_name="perfil",
            name="data_atualizacao",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="perfil",
            name="data_criacao",
            field=models.DateTimeField(
                auto_now_add=True,
                default=datetime.datetime(
                    2025, 5, 13, 0, 56, 4, 910233, tzinfo=datetime.UTC
                ),
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="perfil",
            name="matricula",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="logatividade",
            name="acao",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="logatividade",
            name="detalhes",
            field=models.TextField(default="Sem detalhes"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="logatividade",
            name="usuario",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="perfil",
            name="foto",
            field=models.ImageField(blank=True, null=True, upload_to="fotos_perfil/"),
        ),
        migrations.AlterField(
            model_name="perfil",
            name="status",
            field=models.CharField(
                choices=[
                    ("pendente", "Pendente"),
                    ("aprovado", "Aprovado"),
                    ("rejeitado", "Rejeitado"),
                ],
                default="pendente",
                max_length=10,
            ),
        ),
    ]
