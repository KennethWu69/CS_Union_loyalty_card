# Generated by Django 3.2.9 on 2021-12-09 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loyalty_card', '0018_cck_flg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cck',
            name='flg',
        ),
    ]