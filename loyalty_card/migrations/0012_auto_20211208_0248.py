# Generated by Django 3.2.9 on 2021-12-07 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loyalty_card', '0011_auto_20211208_0124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sheet',
            name='cellphone',
        ),
        migrations.RemoveField(
            model_name='sheet',
            name='email',
        ),
        migrations.RemoveField(
            model_name='sheet',
            name='grade',
        ),
        migrations.RemoveField(
            model_name='sheet',
            name='name',
        ),
    ]
