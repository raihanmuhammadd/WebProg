# Generated by Django 5.0.4 on 2024-07-07 03:08

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpem', '0002_alter_attendingcourse_attending_course_id_and_more'),
    ]

    operations = [
        migrations.RenameIndex(
            model_name='accountuser',
            new_name='webpem_acco_account_c29ec3_idx',
            old_name='webpem_acco_account_9e91ba_idx',
        ),
        migrations.AlterField(
            model_name='accountuser',
            name='account_user_related_user',
            field=models.CharField(editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='accountuser',
            name='account_user_updated_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='attendingcourse',
            name='attending_course_id',
            field=models.UUIDField(default=uuid.UUID('dc32aef3-9b6e-4ba3-ad18-bf5077072d5e'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_id',
            field=models.UUIDField(default=uuid.UUID('65c70d5a-16ed-44fb-bdb1-3a58e9c39118'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
