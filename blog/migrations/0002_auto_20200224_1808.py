# Generated by Django 3.0.2 on 2020-02-24 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RedSocial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('clases', models.TextField()),
            ],
            options={
                'verbose_name': 'RedSocial',
                'verbose_name_plural': 'RedesSociales',
            },
        ),
        migrations.AddField(
            model_name='categoria',
            name='activo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='configuracionbasica',
            name='activo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='post',
            name='activo',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='enlace',
            name='link',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='enlace',
            name='tipo',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.RedSocial'),
        ),
    ]
