# Generated by Django 3.0.7 on 2021-04-06 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location_register', '0021_auto_20210330_1650'),
        ('business_register', '0080_auto_20210405_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='sanction',
            name='company',
            field=models.ForeignKey(blank=True, default=None, help_text='company or organisation under this sanction', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='official_sanctions', to='business_register.Company', verbose_name='company'),
        ),
        migrations.AddField(
            model_name='sanction',
            name='country_of_origin',
            field=models.ForeignKey(help_text='country of citizenship/registration of the person or company under sanctions', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sanctions_applied_to_residents', to='location_register.Country', verbose_name='country of origin'),
        ),
        migrations.AddField(
            model_name='sanction',
            name='is_confirmed',
            field=models.BooleanField(default=False, help_text='identity of the PEP or company under this sanction is confirmed', verbose_name='is_confirmed'),
        ),
        migrations.AddField(
            model_name='sanction',
            name='pep',
            field=models.ForeignKey(blank=True, default=None, help_text='politically exposed person under this sanction', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='official_sanctions', to='business_register.Pep', verbose_name='PEP'),
        ),
        migrations.AlterField(
            model_name='sanction',
            name='country',
            field=models.ForeignKey(blank=True, default=None, help_text='country under this sanction', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='official_sanctions', to='location_register.Country', verbose_name='country'),
        ),
    ]