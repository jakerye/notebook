# Generated by Django 2.0.5 on 2018-05-10 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0002_auto_20180510_1354'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Votes',
            new_name='Vote',
        ),
    ]
