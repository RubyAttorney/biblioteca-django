# Generated by Django 4.1.4 on 2022-12-10 20:07

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimos', '0010_alter_livros_autor_alter_livros_editora_emprestimo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='codigo',
            field=models.BigIntegerField(auto_created=True, primary_key=builtins.id, serialize=False),
        ),
    ]
