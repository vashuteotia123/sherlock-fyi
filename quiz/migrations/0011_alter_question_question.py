# Generated by Django 3.2.7 on 2021-09-21 18:34

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0010_alter_question_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
