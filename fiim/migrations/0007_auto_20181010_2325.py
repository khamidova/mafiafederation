# Generated by Django 2.0.5 on 2018-10-10 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fiim', '0006_add_contacts_to_official'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='participant',
            field=models.ManyToManyField(blank=True, related_name='documents', to='fiim.Official'),
        ),
        migrations.AlterField(
            model_name='official',
            name='document',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='fiim.Document'),
        ),
    ]