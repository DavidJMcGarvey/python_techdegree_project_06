# Generated by Django 2.2.1 on 2019-05-16 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mineral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250)),
                ('image_filename', models.CharField(blank=True, max_length=250)),
                ('image_caption', models.CharField(blank=True, max_length=250)),
                ('category', models.CharField(blank=True, max_length=250)),
                ('formula', models.CharField(blank=True, max_length=250)),
                ('strunz_classification', models.CharField(blank=True, max_length=250)),
                ('color', models.CharField(blank=True, max_length=250)),
                ('crystal_system', models.CharField(blank=True, max_length=250)),
                ('unit_cell', models.CharField(blank=True, max_length=250)),
                ('crystal', models.CharField(blank=True, max_length=250)),
                ('symmetry', models.CharField(blank=True, max_length=250)),
                ('cleavage', models.CharField(blank=True, max_length=250)),
                ('mohs_scale_hardness', models.CharField(blank=True, max_length=250)),
                ('luster', models.CharField(blank=True, max_length=250)),
                ('streak', models.CharField(blank=True, max_length=250)),
                ('diaphaneity', models.CharField(blank=True, max_length=250)),
                ('optical_properties', models.CharField(blank=True, max_length=250)),
                ('refractive_index', models.CharField(blank=True, max_length=250)),
                ('crystal_habit', models.CharField(blank=True, max_length=250)),
                ('specific_gravity', models.CharField(blank=True, max_length=250)),
            ],
        ),
    ]
