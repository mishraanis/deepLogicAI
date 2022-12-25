from django.db import models

# Create your models here.
from django.db import models


class PdfDocument(models.Model):
    file = models.FileField(upload_to="documents/pdf", null=True, blank=True)  # for creating file input
    text = models.TextField(null=True, blank=True)
    owner = models.ForeignKey('auth.User', related_name='pdfs', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.file.name


class JpgDocument(models.Model):
    image = models.ImageField(upload_to="documents/jpg", null=True, blank=True)  # for creating file input
    text = models.TextField(null=True, blank=True)
    owner = models.ForeignKey('auth.User', related_name='jpgs', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.image.name
