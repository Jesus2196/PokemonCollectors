# Generated by Django 3.2.7 on 2021-11-03 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('level', models.IntegerField(default=0)),
                ('element', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
            ],
        ),
    ]
