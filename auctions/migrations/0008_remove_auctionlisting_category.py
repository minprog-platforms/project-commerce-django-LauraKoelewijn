# Generated by Django 4.1.3 on 2022-12-07 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auctionlisting_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionlisting',
            name='category',
        ),
    ]
