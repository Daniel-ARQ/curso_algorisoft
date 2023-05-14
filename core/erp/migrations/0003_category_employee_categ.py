# Generated by Django 4.2.1 on 2023-05-09 14:47

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0002_type_employee_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
                'ordering': [builtins.id],
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='categ',
            field=models.ManyToManyField(to='erp.category'),
        ),
    ]
