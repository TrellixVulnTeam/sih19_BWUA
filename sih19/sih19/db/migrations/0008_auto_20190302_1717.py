# Generated by Django 2.1.7 on 2019-03-02 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0007_auto_20190302_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='latitude',
            field=models.FloatField(default=82.9739),
        ),
        migrations.AddField(
            model_name='region',
            name='longitude',
            field=models.FloatField(default=25.3176),
        ),
    ]