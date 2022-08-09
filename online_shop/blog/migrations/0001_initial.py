# Generated by Django 4.1 on 2022-08-09 08:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=80)),
                ('post_Slug', models.SlugField(max_length=100)),
                ('post_descripton', models.TextField()),
                ('post_created', models.DateTimeField(auto_now_add=True)),
                ('post_updated', models.DateTimeField(auto_now=True)),
                ('post_status', models.CharField(choices=[('published', 'Published'), ('draft', 'Draft')], default='draft', max_length=80)),
                ('post_published', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]