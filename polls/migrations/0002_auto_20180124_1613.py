# Generated by Django 2.0 on 2018-01-24 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
