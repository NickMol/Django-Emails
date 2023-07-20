# Generated by Django 4.2.3 on 2023-07-16 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=500)),
                ('message', models.TextField(max_length=500)),
                ('email', models.EmailField(max_length=254)),
                ('icoon', models.TextField(blank=True, max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('edited_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]