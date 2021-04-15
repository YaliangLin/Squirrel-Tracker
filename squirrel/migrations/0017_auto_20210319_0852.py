# Generated by Django 3.1.7 on 2021-03-19 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squirrel', '0016_auto_20210319_0527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biaoge',
            name='profile_image',
            field=models.ImageField(help_text='Profile picture of pet', null=True, upload_to='img/'),
        ),
        migrations.AlterField(
            model_name='images',
            name='profile_image',
            field=models.ImageField(blank=True, help_text='Profile picture of pet', upload_to='img/'),
        ),
    ]
