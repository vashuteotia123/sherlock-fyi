# Generated by Django 3.2.7 on 2021-09-21 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_auto_20190210_0739'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='level',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
