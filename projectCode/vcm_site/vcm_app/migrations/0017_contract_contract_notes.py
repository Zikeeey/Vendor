# Generated by Django 3.2.9 on 2021-12-12 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vcm_app', '0016_rename_contract_status_vendor_vendor_referral'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='contract_notes',
            field=models.TextField(blank=True),
        ),
    ]
