# Generated by Django 4.2.5 on 2023-10-20 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0005_alter_weightgoal_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watergoal',
            name='liters',
            field=models.FloatField(),
        ),
    ]