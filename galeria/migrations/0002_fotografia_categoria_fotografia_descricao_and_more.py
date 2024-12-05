# Generated by Django 5.1 on 2024-09-12 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('NEBULOSA', 'Nebulosa'), ('GALÁXIA', 'Galáxia'), ('ESTRELA', 'Estrela'), ('PLANETA', 'Planeta')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='fotografia',
            name='descricao',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='fotografia',
            name='legenda',
            field=models.CharField(max_length=100),
        ),
    ]