# Generated by Django 3.1 on 2020-08-22 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200822_1850'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CannabisSmoke',
        ),
        migrations.DeleteModel(
            name='Hobbies',
        ),
    ]