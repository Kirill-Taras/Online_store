# Generated by Django 4.2.10 on 2024-04-05 13:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_alter_blog_count_views_alter_blog_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 5, 13, 11, 20, 397854),
                verbose_name="Дата создания",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="updated_at",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 5, 13, 11, 20, 397863),
                verbose_name="Дата последнего изменения",
            ),
        ),
    ]
