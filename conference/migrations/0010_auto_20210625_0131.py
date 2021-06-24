# Generated by Django 3.2 on 2021-06-24 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0009_receivedexception'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailQueue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corresponding_id', models.CharField(blank=True, default='unknown', max_length=1000)),
                ('mail_reason', models.CharField(blank=True, default='unknown', max_length=10000)),
                ('general_info', models.CharField(blank=True, default='unknown', max_length=10000)),
            ],
        ),
        migrations.AlterField(
            model_name='receivedexception',
            name='function_name',
            field=models.CharField(blank=True, default='unknown', max_length=1000),
        ),
    ]