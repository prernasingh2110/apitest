# Generated by Django 2.1.3 on 2018-12-03 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview1', '0002_auto_20181203_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='accuracy',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
