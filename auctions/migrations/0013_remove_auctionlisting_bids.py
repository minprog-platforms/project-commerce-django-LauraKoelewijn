# Generated by Django 4.1.3 on 2022-12-10 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_alter_auctionlisting_current_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionlisting',
            name='bids',
        ),
    ]
