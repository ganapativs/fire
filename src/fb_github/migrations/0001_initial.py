# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 19:12
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import fb_github.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fb_emails', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('login', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('gh_data', django.contrib.postgres.fields.jsonb.JSONField()),
                ('issue_number', models.PositiveIntegerField()),
                ('msg', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fb_emails.IncomingMessage')),
            ],
        ),
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('email_slug', models.SlugField(default=fb_github.models.email_slug_default)),
                ('inviter_login', models.CharField(max_length=200)),
                ('login', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('original_invitation_data', django.contrib.postgres.fields.jsonb.JSONField()),
                ('status', models.CharField(choices=[('pending-accept', 'Pending accept'), ('pending-inviter-approval', 'Pending inviter approval'), ('active', 'Active')], default='pending-accept', max_length=32)),
                ('admins', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Repositories',
            },
        ),
        migrations.AddField(
            model_name='issue',
            name='repo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fb_github.Repository'),
        ),
        migrations.AddField(
            model_name='emailmap',
            name='repo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fb_github.Repository'),
        ),
        migrations.AddField(
            model_name='emailmap',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='repository',
            unique_together=set([('login', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='emailmap',
            unique_together=set([('repo', 'email')]),
        ),
    ]
