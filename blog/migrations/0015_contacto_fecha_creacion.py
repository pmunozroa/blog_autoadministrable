# Generated by Django 3.0.3 on 2020-02-27 20:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20200226_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
