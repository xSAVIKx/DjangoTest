# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20141030_0725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='praepostor',
            field=models.ForeignKey(related_name='praepostor', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='students.Student', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.ForeignKey(related_name='groups', on_delete=django.db.models.deletion.SET_NULL, to='students.Group', null=True),
            preserve_default=True,
        ),
    ]
