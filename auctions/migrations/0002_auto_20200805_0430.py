# Generated by Django 3.0.7 on 2020-08-05 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watchlist',
            old_name='watchlist',
            new_name='auction',
        ),
    ]
