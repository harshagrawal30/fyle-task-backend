# Generated by Django 4.1.5 on 2023-01-14 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('avatar', models.FileField(blank=True, upload_to='avatars')),
                ('location', models.TextField(blank=True)),
                ('bio', models.TextField(blank=True)),
                ('twitter', models.CharField(blank=True, max_length=200)),
                ('linkedin', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='repositories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_repositories', to='userRepos.user')),
            ],
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=50)),
                ('repositories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='repository_language', to='userRepos.repositories')),
            ],
        ),
    ]
