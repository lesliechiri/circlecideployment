# Generated by Django 2.2.1 on 2019-05-24 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='number_of_children',
            field=models.IntegerField(),
        ),
    ]
