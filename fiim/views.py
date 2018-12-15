from django.shortcuts import render
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.contrib import messages
from .models import DocumentType, Partner, Official
from .forms import ContactForm
from mafiafederation.settings import DEFAULT_FROM_EMAIL


def documents_list(request):
    document_types = DocumentType.objects.filter(published=True)
    return render(request, 'fiim/documents.html', {'document_types': document_types})


def partners_list(request):
    partners = Partner.objects.all()
    return render(request, 'fiim/partners.html', {'partners': partners})


def officials_list(request):
    officials = Official.objects.filter(published=True).order_by('started_at')
    return render(request, 'fiim/officials.html', {'officials': officials})


def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            subject = request.POST.get('subject', '')
            message = request.POST.get('message', '')

            # Email the profile with the
            # contact information
            template = get_template('fiim/contact_template.txt')
            context = {
                'name': name,
                'email': email,
                'subject': subject,
                'message': message,
            }
            content = template.render(context)
            EmailMessage()
            email = EmailMessage(
                "Mafiafederation.org: Contact form submission",
                content,
                DEFAULT_FROM_EMAIL,
                [email, DEFAULT_FROM_EMAIL],
                headers={'Reply-To': email}
            )
            try:
                email.send()
            except Exception:
                messages.add_message(request, messages.ERROR,
                                     'Произошла ошибка при отправке сообщения. Попробуйте позже.')
            else:
                messages.add_message(request, messages.SUCCESS, 'Сообщение успешно отправлено.')

            return render(request, 'fiim/contact.html', {
                'form': form_class,
            })

    return render(request, 'fiim/contact.html', {
        'form': form_class,
    })
