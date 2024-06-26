# Generated by Django 4.2.7 on 2024-04-06 17:29

import datetime
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
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='название')),
                ('body', models.TextField(verbose_name='содержимое')),
                ('photo', models.ImageField(upload_to='publications/', verbose_name='фото')),
                ('pub_date', models.DateField(default=datetime.datetime.now, verbose_name='дата публикации')),
                ('is_pay', models.BooleanField(default=False, verbose_name='платная публикация')),
                ('is_active', models.BooleanField(default=True, verbose_name='статус')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='автор публикации')),
            ],
            options={
                'verbose_name': 'Публикация',
                'verbose_name_plural': 'Публикации',
            },
        ),
    ]
