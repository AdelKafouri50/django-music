# Generated by Django 3.1.7 on 2021-03-21 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('netflix', '0002_auto_20210315_1424'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='year',
            new_name='artist',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='video',
            new_name='src',
        ),
    ]
