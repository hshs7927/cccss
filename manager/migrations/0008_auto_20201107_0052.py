# Generated by Django 3.1.3 on 2020-11-06 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0007_auto_20201107_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store_set',
            name='openday',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='store_set',
            name='opentime',
            field=models.DateTimeField(),
        ),
    ]
