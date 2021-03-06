# Generated by Django 3.0.7 on 2021-02-15 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20210211_0935'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'verbose_name': 'notification', 'verbose_name_plural': 'notifications'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'question', 'verbose_name_plural': 'questions'},
        ),
        migrations.AlterField(
            model_name='question',
            name='answered',
            field=models.BooleanField(default=False, verbose_name='was answered'),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.TextField(max_length=500, verbose_name='text'),
        ),
    ]
