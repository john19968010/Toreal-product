# Generated by Django 3.0.8 on 2020-08-10 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TOREAL', '0006_card'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactform',
            old_name='passward',
            new_name='password',
        ),
    ]
