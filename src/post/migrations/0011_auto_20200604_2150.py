# Generated by Django 3.0.7 on 2020-06-04 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_auto_20200525_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
