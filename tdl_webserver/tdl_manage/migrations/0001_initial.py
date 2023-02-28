# Generated by Django 4.0.7 on 2023-02-28 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_ID', models.CharField(max_length=3)),
                ('project', models.CharField(max_length=30)),
                ('iformat', models.CharField(max_length=20)),
                ('current', models.CharField(max_length=300)),
                ('stage', models.CharField(max_length=5)),
                ('dependencies', models.CharField(max_length=30)),
            ],
        ),
    ]
