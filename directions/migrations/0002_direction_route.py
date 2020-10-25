# Generated by Django 3.1.2 on 2020-10-25 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('routes', '0001_initial'),
        ('directions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='direction',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='directions', to='routes.route'),
        ),
    ]
