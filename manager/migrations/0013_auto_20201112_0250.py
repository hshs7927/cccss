# Generated by Django 3.1.3 on 2020-11-11 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0012_auto_20201111_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='biz_url',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.CreateModel(
            name='Today_lineup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('set_day', models.DateField()),
                ('quota', models.IntegerField()),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='manager.allitem')),
            ],
        ),
    ]
