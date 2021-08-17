# Generated by Django 3.2.6 on 2021-08-14 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kanvas1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kanvas1.course')),
                ('user_id', models.ManyToManyField(to='kanvas1.User')),
            ],
        ),
    ]
