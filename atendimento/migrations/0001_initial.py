# Generated by Django 3.1.3 on 2020-11-29 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AtendimentoItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id1', models.IntegerField()),
                ('coordenador', models.CharField(max_length=100)),
                ('assunto', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('data', models.CharField(max_length=20)),
            ],
        ),
    ]
