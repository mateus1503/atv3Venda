# Generated by Django 5.0.6 on 2024-06-03 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Venda', '0010_remove_produto_image_produto_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(upload_to='produto_imagens/'),
        ),
    ]
