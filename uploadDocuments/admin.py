from django.contrib import admin

# Register your models here.

from .models import PdfDocument, JpgDocument

admin.site.register(PdfDocument)
admin.site.register(JpgDocument)