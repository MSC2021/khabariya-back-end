# Generated by Django 3.1.5 on 2021-01-20 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='imagesmodel',
            name='newsArticle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='newsapp.newsarticle'),
        ),
    ]