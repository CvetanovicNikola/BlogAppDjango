# Generated by Django 2.2 on 2019-05-14 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20190514_1335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='downVotes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='upVotes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='voted',
        ),
    ]
