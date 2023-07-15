from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from django.core.mail import EmailMessage
from io import BytesIO
from xhtml2pdf import pisa
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'library/book_detail.html', {'book': book})

def generate_pdf(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    template_path = 'library/invoice.html'
    context = {
        'book': book,
    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="book_details.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Error al generar el PDF', status=500)
    return response

def send_email(request, book_id):
    if request.method == 'POST':
        pdf = generate_pdf(request, book_id)
        email_address = request.POST.get('email')

        email = EmailMessage(
            'Detalles del libro',
            'Adjunto encontrarás los detalles del libro en formato PDF.',
            'melsy@gmail.com',
            [email_address]
        )

        email.attach('book_details.pdf', pdf.getvalue(), 'application/pdf')
        email.send()

        return render(request, 'library/email_sent.html')

    # Si no es una solicitud POST, renderizar la página de detalles del libro
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'library/book_detail.html', {'book': book})

