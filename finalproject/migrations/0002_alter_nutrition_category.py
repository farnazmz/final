# Generated by Django 4.1.6 on 2023-03-06 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalproject', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nutrition',
            name='category',
            field=models.CharField(choices=[('Protein', 'Protein: Max 50g'), ('Fat', 'Fat: Max 65g'), ('SaturatedFattyAcids', 'Saturated Fatty Acids: Max 20g'), ('Carbohydrates', 'Carbohydrates: Max 304g'), ('Sugars', 'Sugars: Max 38g'), ('Sodium', 'Sodium: Max 2.3g'), ('DietaryFibre', 'DietaryFibre: Max 25g')], default='Protein', max_length=50),
        ),
    ]
