# Generated by Django 4.2.2 on 2023-06-19 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_challenge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='challenge_type',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='status',
            field=models.CharField(default='pending', max_length=20),
        ),
    ]