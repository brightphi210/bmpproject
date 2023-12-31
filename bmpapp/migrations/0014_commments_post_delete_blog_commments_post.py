# Generated by Django 4.1.3 on 2023-05-21 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bmpapp', '0013_remove_blog_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('date_addded', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('intro', models.TextField()),
                ('body', models.TextField()),
                ('date_addded', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.AddField(
            model_name='commments',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bmpapp.post'),
        ),
    ]
