# Generated by Django 3.1 on 2020-08-22 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
        ('accounts', '0003_auto_20200822_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='favourite_cannabis_smoke',
            field=models.ManyToManyField(blank=True, null=True, related_name='profiles', to='master.CannabisSmoke'),
        ),
    ]