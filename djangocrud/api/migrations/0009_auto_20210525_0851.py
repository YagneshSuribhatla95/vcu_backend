# Generated by Django 3.1.3 on 2021-05-25 12:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0008_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='status',
            name='username',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]
