# Generated by Django 2.1.5 on 2020-05-15 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_order'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order',
            new_name='Cart',
        ),
    ]
