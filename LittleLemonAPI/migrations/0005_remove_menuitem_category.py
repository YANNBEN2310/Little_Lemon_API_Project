# Generated by Django 4.1.7 on 2023-03-14 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonAPI', '0004_alter_menuitem_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='category',
        ),
    ]
