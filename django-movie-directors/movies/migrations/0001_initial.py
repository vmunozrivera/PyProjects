# Generated by Django 4.0.5 on 2022-06-27 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('birth', models.DateField(blank=True, null=True)),
                ('dead', models.DateField(blank=True, null=True)),
                ('bio', models.TextField()),
                ('image', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('resume', models.TextField()),
                ('duration', models.PositiveIntegerField()),
                ('image', models.URLField()),
                ('year', models.PositiveIntegerField()),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.director')),
            ],
        ),
    ]
