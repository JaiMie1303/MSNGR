# Generated by Django 3.2 on 2024-03-07 13:26

from django.db import migrations, models
import django.db.models.deletion
import easy_thumbnails.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('avatar', easy_thumbnails.fields.ThumbnailerImageField(default='djangochatserver/default.jpg', upload_to='djangochatserver')),
                ('avatar_small', easy_thumbnails.fields.ThumbnailerImageField(default='djangochatserver/default_small.jpg', upload_to='djangochatserver')),
                ('online', models.BooleanField(default=False)),
                ('room', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='apichat.room')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apichat.userprofile')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apichat.room')),
            ],
        ),
    ]
