# Generated by Django 3.2.6 on 2021-08-14 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_rename_notes_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='date_created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
