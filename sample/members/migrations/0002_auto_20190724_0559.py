# Generated by Django 2.2.3 on 2019-07-24 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=20, verbose_name='이름'),
        ),
    ]