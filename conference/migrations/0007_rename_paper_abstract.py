# Generated by Django 3.2 on 2021-05-04 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0006_auto_20210504_1906'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Paper',
            new_name='Abstract',
        ),
    ]