# Generated by Django 3.2.8 on 2021-11-01 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_bill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rate',
            name='id',
        ),
        migrations.AlterField(
            model_name='rate',
            name='tierID',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
