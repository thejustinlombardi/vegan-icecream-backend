# Generated by Django 4.0.2 on 2022-02-09 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IceCream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('alternatives', models.CharField(max_length=100)),
                ('site', models.TextField()),
                ('photo_url', models.TextField()),
            ],
        ),
    ]
