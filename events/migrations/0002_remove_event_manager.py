# Generated by Django 4.2.6 on 2023-12-21 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='manager',
        ),
    ]
