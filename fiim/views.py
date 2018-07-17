from django.shortcuts import render
from fiim.models import DocumentType, Partner, Official


def documents_list(request):
    document_types = DocumentType.objects.filter(published=True)
    return render(request, 'fiim/documents.html', {'document_types': document_types})

def partners_list(request):
    partners = Partner.objects.all()
    return render(request, 'fiim/partners.html', {'partners': partners})

def officials_list(request):
    officials = Official.objects.filter(published=True).order_by('started_at')
    return render(request, 'fiim/officials.html', {'officials': officials})
