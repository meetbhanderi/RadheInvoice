# Generated by Django 3.0.7 on 2020-07-07 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_auto_20200701_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Quantity_abbr',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
