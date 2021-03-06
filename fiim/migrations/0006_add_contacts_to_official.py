# Generated by Django 2.0.7 on 2018-07-22 16:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiim', '0005_document_upload_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='official',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='official',
            name='facebook',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='official',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
                regex='^\\+?1?\\d{9,15}$'
            )]),
        ),
        migrations.AddField(
            model_name='official',
            name='vkontakte',
            field=models.URLField(blank=True),
        ),
    ]
