# Generated by Django 3.2.8 on 2021-11-01 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_rename_rate_rate_therange'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rate',
            old_name='theRange',
            new_name='rate',
        ),
    ]
