# Generated by Django 3.0.7 on 2020-07-16 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0002_auto_20200711_1723'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subscribe',
            new_name='Subscription',
        ),
        migrations.RenameField(
            model_name='subscription',
            old_name='email_id',
            new_name='email',
        ),
    ]