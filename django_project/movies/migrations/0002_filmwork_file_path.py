# Generated by Django 3.2 on 2023-03-20 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filmwork',
            name='file_path',
            field=models.TextField(blank=True, null=True, verbose_name='file path'),
        ),
    ]
