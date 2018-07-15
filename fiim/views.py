from django.shortcuts import render
from fiim.models import DocumentType, Partner
from django.db.models.functions import Length


def documents_list(request):
    document_types = DocumentType.objects.filter(published=True)
    return render(request, 'fiim/documents.html', {'document_types': document_types})

def partners_list(request):
    partners = Partner.objects.all()
    return render(request, 'fiim/partners.html', {'partners': partners})
