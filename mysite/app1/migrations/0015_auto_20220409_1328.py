# Generated by Django 2.2 on 2022-04-09 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0014_work_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='userid',
        ),
        migrations.CreateModel(
            name='ManyToManyRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.Applications')),
                ('workid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.Work')),
            ],
        ),
    ]
