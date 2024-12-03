from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.timezone import now
from django.conf import settings
from django.core import mail
from django.template.loader import render_to_string

class Contact(models.Model):
    name = models.CharField('nome', max_length=100)
    phone = models.CharField('telefone', max_length=20, blank=True)
    email = models.EmailField('e-mail')
    message = models.CharField('mensagem', max_length=255)
    created_at = models.DateTimeField('recebido em', auto_now_add=True)
    response = models.TextField('resposta', max_length=200, blank=True, default="")
    reply_created_at = models.DateTimeField('respondido em', blank=True, null=True)
    reply_check = models.BooleanField('respondido?', default=False)
    
    class Meta:
        verbose_name_plural = 'contatos'
        verbose_name = 'contato'
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.email

def _send_mail(template_name, context, subject, from_, to):
    body = render_to_string(template_name, context)
    email = mail.send_mail(subject, body, from_, [from_, to])

@receiver(pre_save, sender=Contact)
def reply(sender, instance, **kwargs):
    #Se instance não tiver uma pk e essa função é chamada ANTES do save(), significa que instance é uma entry nova. A função não deve ser chamada em entries novas.
    if instance.pk:
        previous = sender.objects.get(pk=instance.pk)
        if previous.response != instance.response:
            instance.reply_check = True
            instance.reply_created_at = now()
            _send_mail(
                'contact/contact_response.txt',
                vars(instance),
                'Retorno de contato!',
                settings.DEFAULT_FROM_EMAIL,
                instance.email)