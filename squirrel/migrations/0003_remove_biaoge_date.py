# Generated by Django 3.1.7 on 2021-03-15 23:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squirrel', '0002_auto_20210315_2352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='biaoge',
            name='date',
        ),
    ]