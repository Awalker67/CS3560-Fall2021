# Generated by Django 3.2.8 on 2021-11-01 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_auto_20211031_2159'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rate',
            old_name='rate',
            new_name='theRange',
        ),
    ]
