# Generated by Django 5.2.1 on 2025-05-18 01:37

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Fornecedor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "tipo",
                    models.CharField(
                        choices=[("PF", "Pessoa Física"), ("PJ", "Pessoa Jurídica")],
                        default="PJ",
                        max_length=2,
                        verbose_name="Tipo",
                    ),
                ),
                ("nome", models.CharField(max_length=255, verbose_name="Nome")),
                (
                    "cnpj_cpf",
                    models.CharField(
                        max_length=20, unique=True, verbose_name="CNPJ/CPF"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, null=True, verbose_name="Email"
                    ),
                ),
                (
                    "telefone",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="Telefone"
                    ),
                ),
                (
                    "endereco",
                    models.TextField(blank=True, null=True, verbose_name="Endereço"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Criado em"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Atualizado em"),
                ),
            ],
            options={
                "verbose_name": "Fornecedor",
                "verbose_name_plural": "Fornecedores",
                "ordering": ["nome"],
            },
        ),
    ]
