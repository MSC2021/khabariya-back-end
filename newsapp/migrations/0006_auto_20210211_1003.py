# Generated by Django 3.1.5 on 2021-02-11 10:03

from django.db import migrations, models
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0005_auto_20210211_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='youtube_link',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.URLField(blank=True), blank=True, null=True, size=None),
        ),
    ]
