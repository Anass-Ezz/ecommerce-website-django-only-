# Generated by Django 3.0.8 on 2020-07-19 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0029_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_items',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ManyToManyField(to='ecommerce.Order'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('c', 'consulting'), ('s', 'shipped'), ('w', 'working on it')], default='c', max_length=100),
        ),
    ]
