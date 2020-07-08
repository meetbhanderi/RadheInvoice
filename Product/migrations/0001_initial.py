# Generated by Django 3.0.7 on 2020-07-01 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('ProductName', models.CharField(max_length=50)),
                ('UnitPrice', models.DecimalField(decimal_places=2, max_digits=9)),
                ('CreatedOn', models.DateTimeField()),
                ('UpdatedOn', models.DateTimeField(blank=True)),
            ],
        ),
    ]