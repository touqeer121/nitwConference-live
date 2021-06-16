# Generated by Django 3.2 on 2021-06-16 09:29

import django.core.validators
from django.db import migrations, models
import gdstorage.storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abstract',
            fields=[
                ('abs_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('track', models.CharField(max_length=500)),
                ('prefix', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('is_finally_approved', models.BooleanField(blank=True, default=False)),
                ('is_finally_rejected', models.BooleanField(blank=True, default=False)),
                ('remark', models.CharField(blank=True, default='', max_length=5000)),
                ('is_approved_by_A', models.BooleanField(blank=True, default=False)),
                ('is_rejected_by_A', models.BooleanField(blank=True, default=False)),
                ('is_approved_by_B', models.BooleanField(blank=True, default=False)),
                ('is_rejected_by_B', models.BooleanField(blank=True, default=False)),
                ('remark_A', models.CharField(blank=True, default='', max_length=5000)),
                ('remark_B', models.CharField(blank=True, default='', max_length=5000)),
                ('track_A', models.CharField(blank=True, default='A', max_length=5000, null=True)),
                ('track_B', models.CharField(blank=True, default='admin', max_length=5000, null=True)),
                ('country', models.CharField(blank=True, default='undefined', max_length=5000, null=True)),
                ('state', models.CharField(blank=True, default='undefined', max_length=500, null=True)),
                ('institution', models.CharField(max_length=1000)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=20, validators=[django.core.validators.RegexValidator(message='Invalid Mobile Number', regex='[0-9]{10}')])),
                ('paper_title', models.CharField(max_length=500)),
                ('abstract_pdf', models.FileField(storage=gdstorage.storage.GoogleDriveStorage(), upload_to='maps', validators=[django.core.validators.FileExtensionValidator(['pdf', 'doc', 'docx'])])),
                ('submission_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Author_Type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('author_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ContactUsMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message='Invalid Mobile Number', regex='[0-9]{10}')])),
                ('subject', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=1000)),
                ('has_been_read', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('map_name', models.CharField(max_length=200)),
                ('map_data', models.FileField(storage=gdstorage.storage.GoogleDriveStorage(), upload_to='maps')),
            ],
        ),
        migrations.CreateModel(
            name='Paper_Count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paper_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Registration_Count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Registration_Type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('registration_type', models.CharField(max_length=100)),
            ],
        ),
    ]
