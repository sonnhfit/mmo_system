# Generated by Django 3.1 on 2020-08-09 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20200809_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='facebookuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]