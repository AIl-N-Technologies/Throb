# Generated by Django 5.0.2 on 2024-02-22 20:41

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0019_alter_featureflags_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="verificationcodes",
            options={
                "verbose_name": "Verification Code",
                "verbose_name_plural": "Verification Codes",
            },
        ),
        migrations.AddField(
            model_name="verificationcodes",
            name="token",
            field=models.TextField(default="BZQQWE", editable=False),
        ),
        migrations.AlterField(
            model_name="verificationcodes",
            name="expiry",
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 22, 23, 41, 26, 332896, tzinfo=datetime.timezone.utc)),
        ),
    ]
