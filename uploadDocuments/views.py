from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from uploadDocuments.forms import DocumentForm, JpgDocumentForm
from .models import PdfDocument, JpgDocument
import PyPDF2
from pytesseract import pytesseract
from PIL import Image

def form_upload(request):
    context = {}
    if request.method == 'POST':
        form = request.FILES['document']  # DocumentForm(request.POST, request.FILES)
        fs = FileSystemStorage()
        name = fs.save(form.name, form)
        context['url'] = fs.url(name)
    return render(request, "../templates/uploadDocuments/upload.html", context)


def pdfDocumentList(request):
    documents = PdfDocument.objects.all()
    return render(request, '../templates/uploadDocuments/PdfDocumentList.html', {
        'pdfs': documents
    })


def pdfDocumentUpload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save()
            pdfFileObj = document.file.open('rb')
            pdfReader = PyPDF2.PdfReader(pdfFileObj)
            result = ""
            for i in range(len(pdfReader.pages)):
                pageObj = pdfReader.pages[i]
                result += (pageObj.extract_text()) + '\n'
            pdfFileObj.close()
            document.text = result
            document.owner = request.user
            document.save()
            return redirect('pdfs_list')
    else:
        form = DocumentForm()
    return render(request, '../templates/uploadDocuments/PdfDocumentUpload.html', {
        'form': form
    })


def jpgDocumentList(request):
    documents = JpgDocument.objects.all()
    print(documents)
    return render(request, '../templates/uploadDocuments/JpgDocumentList.html', {
        'images': documents
    })


def jpgDocumentUpload(request):
    if request.method == 'POST':
        form = JpgDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save()
            img = Image.open(document.image)
            path_to_tesseract = r"C:\Users\mishr\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
            pytesseract.tesseract_cmd = path_to_tesseract
            text = pytesseract.image_to_string(img)
            document.text = text
            document.owner = request.user
            document.save()
            return redirect('jpgs_list')
    else:
        form = JpgDocumentForm()
    return render(request, '../templates/uploadDocuments/JpgDocumentUpload.html', {
        'form': form
    })
