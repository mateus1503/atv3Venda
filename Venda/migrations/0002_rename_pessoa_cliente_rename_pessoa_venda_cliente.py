# Generated by Django 5.0.6 on 2024-05-24 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Venda', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pessoa',
            new_name='Cliente',
        ),
        migrations.RenameField(
            model_name='venda',
            old_name='pessoa',
            new_name='cliente',
        ),
    ]
