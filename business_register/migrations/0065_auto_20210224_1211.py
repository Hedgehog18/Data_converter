# Generated by Django 3.0.7 on 2021-02-24 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_register', '0064_auto_20210222_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalpep',
            name='assets_info',
            field=models.TextField(help_text='Info about person`s assets.', null=True, verbose_name='assets info'),
        ),
        migrations.AlterField(
            model_name='historicalpep',
            name='criminal_proceedings',
            field=models.TextField(help_text='Known criminal proceedings against the person.', null=True, verbose_name='known criminal proceedings against the person'),
        ),
        migrations.AlterField(
            model_name='historicalpep',
            name='criminal_record',
            field=models.TextField(help_text='Existing criminal proceeding. If its is null, the person has no sentences against him.', null=True, verbose_name='known sentences against the person'),
        ),
        migrations.AlterField(
            model_name='historicalpep',
            name='date_of_birth',
            field=models.CharField(help_text='Person`s date of birth in YYYY-MM-DD format.', max_length=10, null=True, verbose_name='date of birth'),
        ),
        migrations.AlterField(
            model_name='historicalpep',
            name='fullname',
            field=models.CharField(db_index=True, help_text='Full name "first name middle name last name" in Ukrainian.', max_length=75, verbose_name='full name'),
        ),
        migrations.AlterField(
            model_name='historicalpep',
            name='fullname_transcriptions_eng',
            field=models.TextField(db_index=True, help_text='Full name in English transcription.', verbose_name='options for writing the full name'),
        ),
        migrations.AlterField(
            model_name='historicalpep',
            name='info',
            field=models.TextField(help_text='Additional info about pep.', null=True, verbose_name='additional info'),
        ),
        migrations.AlterField(
            model_name='historicalpep',
            name='is_dead',
            field=models.BooleanField(default=False, help_text='Boolean type. Can be true or false. True - person is dead, false - person is alive.', verbose_name='is_dead'),
        ),
        migrations.AlterField(
            model_name='historicalpep',
            name='is_pep',
            field=models.BooleanField(default=True, help_text='Boolean type. Can be true or false. True - person is politically exposed person, false - person is not politically exposed person.', verbose_name='is pep'),
        ),
        migrations.AlterField(
            model_name='historicalpep',
            name='last_employer',
            field=models.CharField(db_index=True, help_text='Last employer in Ukrainian.', max_length=512, null=True, verbose_name='last office'),
        ),
        migrations.AlterField(
            model_name='historicalpep',
            name='last_job_title',
            field=models.CharField(db_index=True, help_text='Title of the last job in Ukrainian.', max_length=340, null=True, verbose_name='last position'),
        ),
        migrations.AlterField(
            model_name='historicalpep',
            name='place_of_birth',
            field=models.CharField(help_text='The name of the settlement where the person was born.', max_length=100, null=True, verbose_name='place of birth'),
        ),
        migrations.AlterField(
            model_name='historicalpep',
            name='sanctions',
            field=models.TextField(help_text='Known sanctions against the person. If its is null, the person has no sanctions against him.', null=True, verbose_name='known sanctions against the person'),
        ),
        migrations.AlterField(
            model_name='historicalpep',
            name='termination_date',
            field=models.CharField(help_text='PEP status termination date.', max_length=10, null=True, verbose_name='PEP status termination date '),
        ),
        migrations.AlterField(
            model_name='historicalpep',
            name='wanted',
            field=models.TextField(help_text='Information on being wanted. If its null, the person is not on the wanted list.', null=True, verbose_name='wanted'),
        ),
        migrations.AlterField(
            model_name='pep',
            name='assets_info',
            field=models.TextField(help_text='Info about person`s assets.', null=True, verbose_name='assets info'),
        ),
        migrations.AlterField(
            model_name='pep',
            name='criminal_proceedings',
            field=models.TextField(help_text='Known criminal proceedings against the person.', null=True, verbose_name='known criminal proceedings against the person'),
        ),
        migrations.AlterField(
            model_name='pep',
            name='criminal_record',
            field=models.TextField(help_text='Existing criminal proceeding. If its is null, the person has no sentences against him.', null=True, verbose_name='known sentences against the person'),
        ),
        migrations.AlterField(
            model_name='pep',
            name='date_of_birth',
            field=models.CharField(help_text='Person`s date of birth in YYYY-MM-DD format.', max_length=10, null=True, verbose_name='date of birth'),
        ),
        migrations.AlterField(
            model_name='pep',
            name='fullname',
            field=models.CharField(db_index=True, help_text='Full name "first name middle name last name" in Ukrainian.', max_length=75, verbose_name='full name'),
        ),
        migrations.AlterField(
            model_name='pep',
            name='fullname_transcriptions_eng',
            field=models.TextField(db_index=True, help_text='Full name in English transcription.', verbose_name='options for writing the full name'),
        ),
        migrations.AlterField(
            model_name='pep',
            name='info',
            field=models.TextField(help_text='Additional info about pep.', null=True, verbose_name='additional info'),
        ),
        migrations.AlterField(
            model_name='pep',
            name='is_dead',
            field=models.BooleanField(default=False, help_text='Boolean type. Can be true or false. True - person is dead, false - person is alive.', verbose_name='is_dead'),
        ),
        migrations.AlterField(
            model_name='pep',
            name='is_pep',
            field=models.BooleanField(default=True, help_text='Boolean type. Can be true or false. True - person is politically exposed person, false - person is not politically exposed person.', verbose_name='is pep'),
        ),
        migrations.AlterField(
            model_name='pep',
            name='last_employer',
            field=models.CharField(db_index=True, help_text='Last employer in Ukrainian.', max_length=512, null=True, verbose_name='last office'),
        ),
        migrations.AlterField(
            model_name='pep',
            name='last_job_title',
            field=models.CharField(db_index=True, help_text='Title of the last job in Ukrainian.', max_length=340, null=True, verbose_name='last position'),
        ),
        migrations.AlterField(
            model_name='pep',
            name='place_of_birth',
            field=models.CharField(help_text='The name of the settlement where the person was born.', max_length=100, null=True, verbose_name='place of birth'),
        ),
        migrations.AlterField(
            model_name='pep',
            name='sanctions',
            field=models.TextField(help_text='Known sanctions against the person. If its is null, the person has no sanctions against him.', null=True, verbose_name='known sanctions against the person'),
        ),
        migrations.AlterField(
            model_name='pep',
            name='termination_date',
            field=models.CharField(help_text='PEP status termination date.', max_length=10, null=True, verbose_name='PEP status termination date '),
        ),
        migrations.AlterField(
            model_name='pep',
            name='wanted',
            field=models.TextField(help_text='Information on being wanted. If its null, the person is not on the wanted list.', null=True, verbose_name='wanted'),
        ),
        migrations.AddIndex(
            model_name='pep',
            index=models.Index(fields=['fullname', 'date_of_birth'], name='business_re_fullnam_0639b9_idx'),
        ),
        migrations.AddIndex(
            model_name='pep',
            index=models.Index(fields=['updated_at'], name='business_re_updated_cec263_idx'),
        ),
    ]
