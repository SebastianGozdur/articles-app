# Generated by Django 2.0 on 2018-01-14 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articleName', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
