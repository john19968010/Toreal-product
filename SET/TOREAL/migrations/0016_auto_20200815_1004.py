# Generated by Django 3.0.8 on 2020-08-15 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TOREAL', '0015_auto_20200815_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(upload_to='user_image'),
        ),
    ]
