# Generated by Django 3.1.2 on 2020-10-25 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stop_offs', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=200)),
            ],
        ),
    ]
