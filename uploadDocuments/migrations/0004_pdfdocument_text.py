# Generated by Django 4.1.4 on 2022-12-25 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadDocuments', '0003_pdfdocument_delete_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdfdocument',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]