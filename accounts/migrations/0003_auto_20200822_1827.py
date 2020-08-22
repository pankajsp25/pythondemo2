# Generated by Django 3.1 on 2020-08-22 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
        ('accounts', '0002_auto_20200821_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='education',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='master.education'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='favourite_cannabis_smoke',
            field=models.ManyToManyField(blank=True, null=True, to='master.CannabisSmoke'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='hobbies',
            field=models.ManyToManyField(blank=True, null=True, to='master.Hobbies'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='religion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='master.religion'),
        ),
        migrations.DeleteModel(
            name='Education',
        ),
        migrations.DeleteModel(
            name='Religion',
        ),
    ]