# Generated by Django 3.2.2 on 2021-05-10 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contours', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='img',
            name='filtered',
            field=models.ImageField(default=1, upload_to='images'),
            preserve_default=False,
        ),
    ]