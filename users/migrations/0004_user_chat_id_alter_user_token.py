# Generated by Django 4.2.7 on 2024-04-07 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_is_vip_user_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='chat_id',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='телеграм токен'),
        ),
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='токен'),
        ),
    ]