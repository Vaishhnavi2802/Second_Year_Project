# Generated by Django 2.2 on 2022-02-20 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_remove_work_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='applications',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='imagedata'),
        ),
    ]