# Generated by Django 3.2.8 on 2021-11-01 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_remove_customer_fname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='lname',
        ),
        migrations.AddField(
            model_name='customer',
            name='fullName',
            field=models.CharField(default='uknown', max_length=50),
        ),
    ]
