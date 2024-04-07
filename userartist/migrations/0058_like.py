# Generated by Django 4.2.6 on 2024-03-24 01:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userartist', '0057_alter_view1_views_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_count', models.IntegerField(default=0)),
                ('authorlike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authorLike', to=settings.AUTH_USER_MODEL)),
                ('postlike', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='postLike', to='userartist.profile')),
            ],
        ),
    ]