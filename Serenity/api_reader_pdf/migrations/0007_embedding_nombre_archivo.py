# Generated by Django 4.2.2 on 2023-06-15 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_reader_pdf', '0006_remove_embedding_nombre_archivo'),
    ]

    operations = [
        migrations.AddField(
            model_name='embedding',
            name='nombre_archivo',
            field=models.CharField(default='S/N', max_length=100),
        ),
    ]
