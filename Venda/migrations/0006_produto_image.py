# Generated by Django 5.0.6 on 2024-06-03 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Venda', '0005_remove_clientejuridico_cliente_ptr_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='image',
            field=models.ImageField(default=0, upload_to='imagens_produto/'),
            preserve_default=False,
        ),
    ]
