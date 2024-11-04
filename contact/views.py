from django.shortcuts import render
from contact.forms import ContactForm
from django.template.loader import render_to_string
from django.core import mail
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            body = render_to_string('contact/contact_email.txt', form.cleaned_data)
            email = mail.send_mail('Entrando em contato!', body, form.cleaned_data['email'],[form.cleaned_data['email'], 'contato@eventif.com.br'])
            messages.success(request, 'Mensagem enviada com sucesso!')
            return HttpResponseRedirect('/contato/')
        else:
            return render(request, 'contact/contact_form.html', {'form': form})
    else:
        context = {'form': ContactForm()}
        return render(request, 'contact/contact_form.html', context)