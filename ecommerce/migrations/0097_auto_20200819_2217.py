# Generated by Django 3.0.8 on 2020-08-19 21:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0096_auto_20200819_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='after_reduction_total',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.Order'),
        ),
        migrations.AlterField(
            model_name='product',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 19, 22, 17, 20, 922329)),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecommerce.Order'),
        ),
    ]
