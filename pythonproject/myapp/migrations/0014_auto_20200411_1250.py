# Generated by Django 3.0.3 on 2020-04-11 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_auto_20200411_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='author',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
    ]