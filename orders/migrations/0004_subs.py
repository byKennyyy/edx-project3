# Generated by Django 2.1.5 on 2020-05-14 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20200514_1138'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=64)),
                ('small', models.FloatField(default=0)),
                ('large', models.FloatField(default=0)),
            ],
        ),
    ]