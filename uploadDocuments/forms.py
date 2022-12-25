from django import forms
from .models import PdfDocument, JpgDocument


class DocumentForm(forms.ModelForm):
    class Meta:
        model = PdfDocument
        fields = 'file',

class JpgDocumentForm(forms.ModelForm):
    class Meta:
        model = JpgDocument
        fields = 'image',
