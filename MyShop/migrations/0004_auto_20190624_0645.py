# Generated by Django 2.1.7 on 2019-06-24 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyShop', '0003_auto_20190624_0644'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='usern',
            new_name='user',
        ),
    ]