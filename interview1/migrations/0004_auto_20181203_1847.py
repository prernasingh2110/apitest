# Generated by Django 2.1.3 on 2018-12-03 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview1', '0003_auto_20181203_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='lat',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='lng',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True),
        ),
    ]