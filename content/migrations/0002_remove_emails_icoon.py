# Generated by Django 4.2.3 on 2023-07-16 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emails',
            name='icoon',
        ),
    ]
