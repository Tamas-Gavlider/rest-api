# Generated by Django 5.1.4 on 2024-12-20 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='https://res.cloudinary.com/dcyek6elz/image/upload/v1733484651/default_profile_tizd6n.jpg', upload_to='images/'),
        ),
    ]
