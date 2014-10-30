# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=32)),
            ],
            options={
                'ordering': ['title'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=32)),
                ('surname', models.CharField(max_length=32)),
                ('middle_name', models.CharField(max_length=32, blank=True)),
                ('birthday_date', models.DateField(blank=True)),
                ('student_card_id', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, blank=True)),
                ('group', models.ForeignKey(related_name='groups', to='students.Group')),
            ],
            options={
                'ordering': ['surname', 'first_name'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='group',
            name='praepostor',
            field=models.ForeignKey(related_name='praepostor', blank=True, to='students.Student', null=True),
            preserve_default=True,
        ),
    ]
