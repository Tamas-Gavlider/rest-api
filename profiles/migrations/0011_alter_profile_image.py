# Generated by Django 5.1.4 on 2024-12-21 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../cld-sample-5', upload_to='images/'),
        ),
    ]