# Generated by Django 4.2.7 on 2024-04-07 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_options_remove_user_username_user_avatar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_vip',
            field=models.BooleanField(default=False, verbose_name='Вип-клиент'),
        ),
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.PositiveIntegerField(blank=True, max_length=4, null=True, verbose_name='токен'),
        ),
    ]