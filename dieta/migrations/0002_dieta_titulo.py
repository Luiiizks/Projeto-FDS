# Generated by Django 4.2.5 on 2023-10-28 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dieta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dieta',
            name='titulo',
            field=models.TextField(default='Qual Refeição'),
        ),
    ]
