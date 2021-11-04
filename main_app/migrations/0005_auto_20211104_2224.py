# Generated by Django 3.2.7 on 2021-11-04 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_training_exercise'),
    ]

    operations = [
        migrations.CreateModel(
            name='Toy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('effect', models.TextField(max_length=150)),
            ],
        ),
        migrations.AlterModelOptions(
            name='training',
            options={'ordering': ['-date']},
        ),
    ]