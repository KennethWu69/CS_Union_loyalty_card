# Generated by Django 3.2.9 on 2021-12-07 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loyalty_card', '0005_remove_user_info_point'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Github',
        ),
        migrations.DeleteModel(
            name='Hotpot',
        ),
        migrations.DeleteModel(
            name='Machi',
        ),
        migrations.AddField(
            model_name='sheet',
            name='cellphone',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='sheet',
            name='email',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='sheet',
            name='getpoint',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sheet',
            name='grade',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='student_id',
            field=models.CharField(default='', max_length=10),
        ),
    ]
