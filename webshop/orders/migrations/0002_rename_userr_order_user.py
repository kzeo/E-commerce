# Generated by Django 4.1 on 2022-08-23 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='userr',
            new_name='user',
        ),
    ]
