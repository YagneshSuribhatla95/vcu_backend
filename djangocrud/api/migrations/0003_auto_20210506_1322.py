# Generated by Django 3.1.3 on 2021-05-06 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210506_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpcqresponses',
            name='comment1',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='cpcqresponses',
            name='comment2',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
    ]
