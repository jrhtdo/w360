# Generated by Django 4.2.1 on 2023-08-28 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0002_remove_donor_allergies_details_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='full_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
