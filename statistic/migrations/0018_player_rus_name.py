# Generated by Django 3.2.7 on 2021-10-31 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0017_auto_20211030_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='rus_name',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]