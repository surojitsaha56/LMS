# Generated by Django 3.0 on 2021-06-27 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_addbook_bcount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addbook',
            name='bcount',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
    ]
