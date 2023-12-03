# Generated by Django 4.2.4 on 2023-12-03 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CSCI4650850FinalProjectapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagesupload',
            name='image_name',
            field=models.CharField(default='sample', max_length=50),
        ),
        migrations.AddField(
            model_name='imagesupload',
            name='image_type',
            field=models.CharField(choices=[('public', 'PUBLIC'), ('private', 'PRIVATE'), ('animals', 'ANIMALS'), ('flowers', 'FLOWERS')], default='public', max_length=25),
        ),
    ]
