# Generated by Django 3.2.6 on 2021-08-31 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
            ],
        ),
    ]
