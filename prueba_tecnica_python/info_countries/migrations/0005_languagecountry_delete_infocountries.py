# Generated by Django 4.1 on 2022-08-28 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info_countries', '0004_country_remove_infocountries__language'),
    ]

    operations = [
        migrations.CreateModel(
            name='LanguageCountry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_language', models.CharField(max_length=50)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info_countries.country')),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
            },
        ),
        migrations.DeleteModel(
            name='InfoCountries',
        ),
    ]
