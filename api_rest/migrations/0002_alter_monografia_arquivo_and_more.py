# Generated by Django 5.1.7 on 2025-05-21 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monografia',
            name='arquivo',
            field=models.FileField(blank=True, null=True, upload_to='monografias/'),
        ),
        migrations.AlterField(
            model_name='monografia',
            name='coorientador',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
