# Generated by Django 4.0.2 on 2022-02-07 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Today',
            new_name='Day',
        ),
        migrations.AlterModelOptions(
            name='todo',
            options={'verbose_name_plural': 'Todo'},
        ),
    ]
