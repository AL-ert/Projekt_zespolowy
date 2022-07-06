# Generated by Django 4.0.5 on 2022-07-05 10:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wynajem', '0016_alter_samochody_moc_silnika'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zamow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miejsce_odbioru', models.CharField(blank=True, max_length=100, null=True)),
                ('miejsce_oddania', models.CharField(blank=True, max_length=100, null=True)),
                ('data_odbioru', models.DateField(blank=True, null=True)),
                ('data_oddania', models.DateField(blank=True, null=True)),
                ('samochod', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='wynajem.samochody')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]