# Generated by Django 4.2.6 on 2024-03-10 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploadmusic', '0005_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]