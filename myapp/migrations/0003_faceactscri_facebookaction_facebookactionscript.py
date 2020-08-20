# Generated by Django 3.1 on 2020-08-20 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20200816_2043'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacebookAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_code', models.CharField(max_length=50)),
                ('action_name', models.CharField(max_length=255)),
                ('action_desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FacebookActionScript',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('script_code', models.CharField(max_length=50)),
                ('script_name', models.CharField(max_length=255)),
                ('script_desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FaceActScri',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook_action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.facebookaction')),
                ('facebook_action_script', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.facebookactionscript')),
            ],
        ),
    ]