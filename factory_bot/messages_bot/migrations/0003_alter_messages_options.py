# Generated by Django 4.2.5 on 2023-09-30 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messages_bot', '0002_alter_messages_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='messages',
            options={'verbose_name': 'Message', 'verbose_name_plural': 'Messages'},
        ),
    ]
