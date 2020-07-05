# Generated by Django 3.0.2 on 2020-04-18 15:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics', verbose_name='Profile Picture')),
                ('bio', models.CharField(default='', max_length=100)),
                ('gender', models.CharField(blank='true', choices=[('Other', 'Other'), ('Male', 'Male'), ('Female', 'Female')], default='', max_length=10, null='true')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]