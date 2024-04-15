# Generated by Django 4.2.7 on 2024-04-07 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активна'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='publications/', verbose_name='фото'),
        ),
    ]
