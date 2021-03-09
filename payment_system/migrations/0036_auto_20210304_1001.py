# Generated by Django 3.0.7 on 2021-03-04 10:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_system', '0035_auto_20210216_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customsubscriptionrequest',
            name='first_name',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(message="Only alphanumeric characters, digits, and '-. are allowed", regex="^[a-zA-Zа-яА-Я0-9 'іїёєґЄЇҐІЭ.`-]*$"), django.core.validators.RegexValidator(inverse_match=True, message='No more than 2 identical symbols in a row are allowed', regex='(.)\\1{2,}')]),
        ),
        migrations.AlterField(
            model_name='customsubscriptionrequest',
            name='last_name',
            field=models.CharField(max_length=150, validators=[django.core.validators.RegexValidator(message="Only alphanumeric characters, digits, and '-. are allowed", regex="^[a-zA-Zа-яА-Я0-9 'іїёєґЄЇҐІЭ.`-]*$"), django.core.validators.RegexValidator(inverse_match=True, message='No more than 2 identical symbols in a row are allowed', regex='(.)\\1{2,}')]),
        ),
    ]
