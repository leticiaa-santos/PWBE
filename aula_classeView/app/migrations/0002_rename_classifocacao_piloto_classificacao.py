# Generated by Django 5.2 on 2025-04-14 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='piloto',
            old_name='classifocacao',
            new_name='classificacao',
        ),
    ]
