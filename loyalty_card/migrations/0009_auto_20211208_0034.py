# Generated by Django 3.2.9 on 2021-12-07 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loyalty_card', '0008_auto_20211208_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sheet',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]