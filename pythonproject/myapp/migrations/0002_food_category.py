# Generated by Django 3.0.3 on 2020-03-26 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='category',
            field=models.CharField(default='', max_length=30),
        ),
    ]