# Generated by Django 2.0.6 on 2018-07-15 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiim', '0003_add_document_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='published',
            field=models.BooleanField(default=True),
        ),
    ]
