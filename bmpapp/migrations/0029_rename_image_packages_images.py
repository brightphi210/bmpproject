# Generated by Django 4.1.3 on 2023-05-29 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bmpapp', '0028_packages_image_alter_packages_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='packages',
            old_name='image',
            new_name='images',
        ),
    ]