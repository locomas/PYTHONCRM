# Generated by Django 4.2.2 on 2023-07-03 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lead',
            old_name='priotiry',
            new_name='priority',
        ),
    ]
