# Generated by Django 4.1.3 on 2023-05-28 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmpapp', '0025_alter_packages_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packages',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]