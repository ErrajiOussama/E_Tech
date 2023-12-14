# Generated by Django 3.2.3 on 2021-05-26 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Gamme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=1000, null=True)),
                ('image', models.ImageField(blank=True, upload_to='gamme/')),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=50)),
                ('prix', models.FloatField()),
                ('nombre_de_stock', models.IntegerField()),
                ('description', models.CharField(max_length=1000, null=True)),
                ('image', models.ImageField(blank=True, upload_to='products/')),
                ('id_Categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.categorie')),
                ('id_Gamme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.gamme')),
            ],
        ),
    ]