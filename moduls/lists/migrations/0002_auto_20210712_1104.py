# Generated by Django 3.2.5 on 2021-07-12 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='list',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
