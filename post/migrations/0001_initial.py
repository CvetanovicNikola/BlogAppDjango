# Generated by Django 2.2 on 2019-05-14 09:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('image2', models.ImageField(blank=True, upload_to='images/')),
                ('image3', models.ImageField(blank=True, upload_to='images/')),
                ('text', models.TextField()),
                ('text2', models.TextField(blank=True)),
                ('text3', models.TextField(blank=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('title', models.CharField(max_length=250)),
                ('votes', models.IntegerField(default=0)),
                ('voted', models.TextField(blank=True)),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]