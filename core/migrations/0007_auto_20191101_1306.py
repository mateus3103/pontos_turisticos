# Generated by Django 2.2.6 on 2019-11-01 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_pontoturistico_enderecos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontoturistico',
            name='enderecos',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='enderecos.Endereco'),
        ),
    ]
