# Generated by Django 3.0.8 on 2020-08-15 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TOREAL', '0018_auto_20200815_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(upload_to='./static/user_img'),
        ),
    ]
