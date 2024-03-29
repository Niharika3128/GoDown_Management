# Generated by Django 2.1.2 on 2019-03-20 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill_Generation',
            fields=[
                ('bill_id', models.AutoField(primary_key=True, serialize=False)),
                ('vendor_name', models.CharField(max_length=50)),
                ('product_name', models.CharField(max_length=50)),
                ('bill_gen_date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
    ]
