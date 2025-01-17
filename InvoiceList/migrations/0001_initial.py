# Generated by Django 3.0.7 on 2020-07-04 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Order', '0003_auto_20200704_1603'),
        ('Product', '0002_auto_20200701_1559'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('UnitPrice', models.DecimalField(decimal_places=2, max_digits=9)),
                ('AmountTaken', models.DecimalField(decimal_places=2, max_digits=9)),
                ('Discount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('Quantity', models.PositiveSmallIntegerField()),
                ('FinalAmount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('Fk_Order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Order.Order')),
                ('Fk_Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.Product')),
            ],
            options={
                'db_table': 'Product Order',
            },
        ),
    ]
