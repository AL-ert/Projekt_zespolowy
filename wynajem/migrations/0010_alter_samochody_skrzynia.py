# Generated by Django 4.0.5 on 2022-07-02 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wynajem', '0009_alter_samochody_cena'),
    ]

    operations = [
        migrations.AlterField(
            model_name='samochody',
            name='skrzynia',
            field=models.CharField(blank=True, choices=[('0', 'Manualna'), ('1', 'Automat')], max_length=11, null=True),
        ),
    ]