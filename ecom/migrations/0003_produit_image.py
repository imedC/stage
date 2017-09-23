# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0002_remove_produit_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='image',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
