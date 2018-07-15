from django.shortcuts import render
from fiim.models import Document, DOCUMENT_TYPES, Partner
from django.db.models.functions import Length


def documents_list(request):
    documents = {}
    for document_type, _ in DOCUMENT_TYPES:
        documents[document_type] = Document.objects.filter(type=document_type).order_by('created_at')
    return render(request, 'fiim/documents.html', {'documents': documents})

def partners_list(request):
    partners = Partner.objects.all().order_by(Length('name').asc())
    return render(request, 'fiim/partners.html', {'partners': partners})
