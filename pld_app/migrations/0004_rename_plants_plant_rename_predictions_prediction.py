# Generated by Django 4.2.5 on 2023-10-17 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pld_app', '0003_predictions_rename_prediction_result_plants_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Plants',
            new_name='Plant',
        ),
        migrations.RenameModel(
            old_name='Predictions',
            new_name='Prediction',
        ),
    ]
