# Generated by Django 4.2.1 on 2023-05-29 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boardmodel',
            old_name='suthor',
            new_name='author',
        ),
    ]
