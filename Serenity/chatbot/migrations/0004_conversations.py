# Generated by Django 4.2.2 on 2023-06-27 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0003_usuario_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
