# Generated by Django 4.1.3 on 2022-12-07 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auctionlisting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='current_price',
            field=models.FloatField(),
        ),
    ]