# Generated by Django 3.1.7 on 2021-04-15 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_orders'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
    ]
