from django.shortcuts import render
from fiim.models import Document, DOCUMENT_TYPES
import logging
# Create your views here.

def documents_list(request):
    documents = {}
    for document_type, _ in DOCUMENT_TYPES:
        documents[document_type] = Document.objects.filter(type=document_type).order_by('created_at')
    return render(request, 'fiim/documents.html', {'documents': documents})

