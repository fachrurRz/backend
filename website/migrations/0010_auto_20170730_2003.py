# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-30 20:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_taskstatistic_expected_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='expected_amount',
        ),
        migrations.RemoveField(
            model_name='taskstatistic',
            name='expected_amount',
        ),
        migrations.RemoveField(
            model_name='userstatistic',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='userstatistic',
            name='expected_amount',
        ),
        migrations.AddField(
            model_name='task',
            name='expected_amount_alumni',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='expected_amount_capung',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='expected_amount_omega',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='expected_amount_orion',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userstatistic',
            name='amount_alumni',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userstatistic',
            name='amount_capung',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userstatistic',
            name='amount_omega',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userstatistic',
            name='amount_orion',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userstatistic',
            name='task',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='website.Task'),
        ),
        migrations.AlterField(
            model_name='userstatistic',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
