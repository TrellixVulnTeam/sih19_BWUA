# Generated by Django 2.1.7 on 2019-03-03 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0011_auto_20190303_1234'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together=set(),
        ),
    ]