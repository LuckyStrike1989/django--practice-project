# Generated by Django 4.2.15 on 2024-08-21 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='post', verbose_name='썸네일 이미지'),
        ),
    ]
