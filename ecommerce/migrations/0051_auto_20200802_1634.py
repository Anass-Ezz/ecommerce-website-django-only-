# Generated by Django 3.0.8 on 2020-08-02 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0050_auto_20200802_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecommerce.Order'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default='images/default.png', upload_to='images'),
        ),
    ]