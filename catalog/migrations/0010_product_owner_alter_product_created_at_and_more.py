# Generated by Django 4.2.10 on 2024-04-21 13:37

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("catalog", "0009_alter_product_created_at_alter_product_updated_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 21, 13, 37, 33, 536561),
                verbose_name="Дата создания",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="updated_at",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 21, 13, 37, 33, 536569),
                verbose_name="Дата последнего изменения",
            ),
        ),
    ]
