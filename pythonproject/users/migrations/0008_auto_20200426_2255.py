# Generated by Django 3.0.2 on 2020-04-26 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200422_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank='true', choices=[('Female', 'Female'), ('Other', 'Other'), ('Male', 'Male')], default='', max_length=10, null='true'),
        ),
    ]