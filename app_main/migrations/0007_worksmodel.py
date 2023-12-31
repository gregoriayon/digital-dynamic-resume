# Generated by Django 4.2.4 on 2023-08-30 20:06

import ckeditor_uploader.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0006_remove_infomodel_link_insta_infomodel_link_scholar'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorksModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=155, null=True)),
                ('company', models.CharField(max_length=155, null=True, verbose_name='Company Name')),
                ('link', models.URLField(blank=True, default='https://www.google.com/', null=True, verbose_name='Company Link')),
                ('job_start_date', models.DateField(default=django.utils.timezone.now)),
                ('job_end_date', models.DateField(blank=True, null=True)),
                ('details', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Job Summary')),
            ],
            options={
                'verbose_name': 'Work History',
                'verbose_name_plural': 'Works History',
                'ordering': ['-id'],
            },
        ),
    ]
