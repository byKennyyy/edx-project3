# Generated by Django 2.1.5 on 2020-05-14 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_topping'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regular_pizza',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Topping'),
        ),
        migrations.AlterField(
            model_name='sicilian_pizza',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Topping'),
        ),
    ]