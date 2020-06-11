# Generated by Django 2.1.5 on 2020-05-15 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_cart_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=999)),
                ('price', models.FloatField()),
            ],
        ),
    ]