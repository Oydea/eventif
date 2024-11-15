from django.shortcuts import render
from contact.forms import ContactForm
from django.template.loader import render_to_string
from django.core import mail
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.conf import settings
# Create your views here.
#Se o metodo do request for post, faz create, senão faz new
def contact(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def create(request):
    form = ContactForm(request.POST)
    if not form.is_valid():
        return render(request, 'contact/contact_form.html', {'form': form})
    _send_mail(
        'contact/contact_email.txt',
        form.cleaned_data,
        'Entrando em contato!',
        form.cleaned_data['email'],
        settings.DEFAULT_FROM_EMAIL)
    messages.success(request, 'Mensagem enviada com sucesso!')
    return HttpResponseRedirect('/contato/')

    
def new(request):
    return render(request, 'contact/contact_form.html', {'form': ContactForm()})


def _send_mail(template_name, context, subject, from_, to):
    body = render_to_string(template_name, context)
    email = mail.send_mail(subject, body, from_, [from_, to])