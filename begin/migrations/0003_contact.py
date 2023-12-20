# Generated by Django 3.0 on 2020-07-31 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('begin', '0002_delete_videoupload'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sn', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
