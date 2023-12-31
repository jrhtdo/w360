# Generated by Django 4.2.1 on 2023-08-28 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0003_alter_donor_full_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donor',
            name='email',
        ),
        migrations.AddField(
            model_name='donor',
            name='email_address',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='guardians_contact',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
