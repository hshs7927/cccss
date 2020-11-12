# Generated by Django 3.1.3 on 2020-11-06 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0008_auto_20201107_0052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store_set',
            name='store',
        ),
        migrations.AddField(
            model_name='store_set',
            name='store_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.store'),
        ),
    ]
