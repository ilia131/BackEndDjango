# Generated by Django 4.2.6 on 2024-03-09 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userartist', '0036_comment_post1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='artistname',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]