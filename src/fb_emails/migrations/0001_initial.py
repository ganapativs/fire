# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 19:12
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import fb_emails.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_id', models.CharField(max_length=100)),
                ('content_type', models.CharField(max_length=100)),
                ('file', models.FileField(max_length=500, upload_to=fb_emails.models.attachment_file_name)),
            ],
        ),
        migrations.CreateModel(
            name='IncomingMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_html', models.TextField()),
                ('body_text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('from_email', models.EmailField(max_length=200)),
                ('from_name', models.CharField(max_length=200)),
                ('original_post_data', django.contrib.postgres.fields.jsonb.JSONField()),
                ('processed_at', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('pending', 'Pending processing'), ('unrecognized-domain', 'Unrecognized domain'), ('unrecognized-username', 'Unrecognized username'), ('issue-error', 'Failed creating issue'), ('processed', 'Processed')], default='pending', max_length=32)),
                ('subject', models.CharField(max_length=500)),
                ('to_email', models.EmailField(max_length=200)),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
            ],
        ),
        migrations.AddField(
            model_name='attachment',
            name='msg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fb_emails.IncomingMessage'),
        ),
    ]
