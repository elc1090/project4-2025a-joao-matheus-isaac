# Generated by Django 5.2.1 on 2025-06-23 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_lutadores', '0002_lutador_hash_imagem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lutador',
            name='hash_imagem',
        ),
        migrations.AddField(
            model_name='lutador',
            name='url_imagem',
            field=models.URLField(blank=True, null=True),
        ),
    ]
