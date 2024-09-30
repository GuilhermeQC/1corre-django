# Generated by Django 5.1.1 on 2024-09-30 14:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=8)),
                ('road', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=6, null=True)),
                ('neighborhood', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['city'],
            },
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tel', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80)),
                ('sec_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('birth_date', models.DateField()),
                ('cpf', models.CharField(max_length=11)),
                ('user', models.CharField(max_length=120)),
                ('email', models.CharField(max_length=120)),
                ('password', models.CharField(max_length=120)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='umcorre.endereco')),
                ('phone_number', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='umcorre.telefone')),
            ],
            options={
                'ordering': ['first_name', 'sec_name', 'last_name'],
            },
        ),
        migrations.CreateModel(
            name='Freelancer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pessoa_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='umcorre.pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pessoa_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='umcorre.pessoa')),
            ],
        ),
    ]
