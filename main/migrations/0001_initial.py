# Generated by Django 3.0 on 2020-08-02 07:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
                ('edition', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=50)),
                ('book_image', models.ImageField(upload_to='book_pic')),
                ('phone', models.CharField(default='', max_length=20)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]