# Generated by Django 2.2 on 2019-05-14 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20190514_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='price',
            field=models.CharField(default='Dogovor', max_length=250),
        ),
    ]
