# Generated by Django 4.0.5 on 2022-07-05 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wynajem', '0017_zamow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zamow',
            name='data_odbioru',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='zamow',
            name='data_oddania',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]