# Generated by Django 2.1.2 on 2019-03-20 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gd_accountant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill_generation',
            name='status',
            field=models.CharField(default=False, max_length=30),
        ),
    ]