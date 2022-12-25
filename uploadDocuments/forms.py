from django import forms
from .models import PdfDocument, JpgDocument


class DocumentForm(forms.ModelForm):
    class Meta:
        model = PdfDocument
        fields = 'file', 'owner', 'text'

class JpgDocumentForm(forms.ModelForm):
    class Meta:
        model = JpgDocument
        fields = 'image', 'owner', 'text'
