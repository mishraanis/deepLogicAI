# Generated by Django 4.1.4 on 2022-12-25 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadDocuments', '0002_document_email_document_file_document_firstname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PdfDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='documents/pdf')),
            ],
        ),
        migrations.DeleteModel(
            name='Document',
        ),
    ]