# Generated by Django 3.0.2 on 2020-02-24 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200224_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='enlace',
            name='size',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
