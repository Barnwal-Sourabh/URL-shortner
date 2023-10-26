# Generated by Django 4.1.2 on 2023-10-25 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LongToShort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_url', models.URLField(max_length=500)),
                ('short_url', models.CharField(max_length=50, unique=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('clicks', models.IntegerField(default=0)),
            ],
        ),
    ]
