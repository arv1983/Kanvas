# Generated by Django 3.2.6 on 2021-08-17 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanvas1', '0015_alter_submission_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='grade',
            field=models.FloatField(null=True),
        ),
    ]
