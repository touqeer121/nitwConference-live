# Generated by Django 3.2 on 2021-06-15 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0012_registration_payment_method'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='is_id_approved',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='is_payment_approved',
        ),
        migrations.AddField(
            model_name='registration',
            name='id_status',
            field=models.CharField(blank=True, default='2', max_length=1),
        ),
        migrations.AddField(
            model_name='registration',
            name='payment_status',
            field=models.CharField(blank=True, default='2', max_length=1),
        ),
    ]
