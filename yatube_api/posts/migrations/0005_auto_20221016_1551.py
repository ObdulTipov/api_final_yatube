# Generated by Django 2.2.16 on 2022-10-16 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20221016_1550'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_name',
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'following'), name='unique_name'),
        ),
    ]