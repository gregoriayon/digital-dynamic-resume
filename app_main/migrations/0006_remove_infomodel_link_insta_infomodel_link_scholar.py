# Generated by Django 4.2.4 on 2023-08-30 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0005_projectsmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infomodel',
            name='link_insta',
        ),
        migrations.AddField(
            model_name='infomodel',
            name='link_scholar',
            field=models.URLField(blank=True, default='https://www.google.com/', null=True, verbose_name='Google Scholar Link'),
        ),
    ]
