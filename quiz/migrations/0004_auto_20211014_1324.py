# Generated by Django 3.2.8 on 2021-10-14 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20211014_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='hiragana_score',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='score',
            name='katakana_score',
            field=models.JSONField(default=dict),
        ),
    ]
