# Generated by Django 2.0.5 on 2018-10-14 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiim', '0007_auto_20181010_2325'),
    ]

    operations = [
        migrations.AddField(
            model_name='documenttype',
            name='sorting_desc',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
