# Generated by Django 2.2 on 2022-02-23 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_auto_20220223_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.FileField(null=True, upload_to='app1/static/imagedata/'),
        ),
    ]