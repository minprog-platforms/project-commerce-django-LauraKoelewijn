# Generated by Django 4.1.3 on 2022-12-10 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='listing',
        ),
    ]