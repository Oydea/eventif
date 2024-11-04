from django.test import TestCase
from django.core import mail
from contact.forms import ContactForm
# Create your tests here.

#Testes pro carregamento da página de contato
class ContactTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/contato/')
        
    def test_get(self):
        self.assertEqual(200, self.resp.status_code)
    
    def test_template(self):
        self.assertTemplateUsed(
            self.resp, 'contact/contact_form.html')
    
    def test_html(self):
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 5)
        self.assertContains(self.resp, '<textarea')
        self.assertContains(self.resp, 'type="text"', 2)
        self.assertContains(self.resp, 'type="email"')
        self.assertContains(self.resp, 'type="submit"')
    
    def test_csrf(self):
        self.assertContains(self.resp, 'csrfmiddlewaretoken')
    
    def test_has_form(self):
        form = self.resp.context['form']
        self.assertSequenceEqual(
            ['name', 'phone', 'email', 'message'], list(form.fields))
        
#Testes pra post válido e pro envio do email
class ContactPostAndSendTest(TestCase):
    def setUp(self):
        data = dict(name="L.O.V.S.", phone="(53)91234-5678", email="foxyoxy87@gmail.com", message="Boa noite, como me inscrevo?")
        self.resp = self.client.post('/contato/', data)

    def test_post(self):
        self.assertEqual(302, self.resp.status_code)

    def test_send_contact_email(self):
        self.assertEqual(1, len(mail.outbox))

    def test_contact_email_subject(self):
        email = mail.outbox[0]
        expect = "Entrando em contato!"
        self.assertEqual(expect, email.subject)
    
    def test_contact_email_from(self):
        email = mail.outbox[0]
        expect = "foxyoxy87@gmail.com"
        self.assertEqual(expect, email.from_email)

    def test_contact_email_to(self):
        email = mail.outbox[0]
        expect = ["foxyoxy87@gmail.com", "contato@eventif.com.br"]
        self.assertQuerySetEqual(expect, email.to)

    def test_contact_email_body(self):
        email = mail.outbox[0]
        self.assertIn('L.O.V.S.', email.body)
        self.assertIn('(53)91234-5678', email.body)
        self.assertIn('foxyoxy87@gmail.com', email.body)
        self.assertIn('Boa noite, como me inscrevo?', email.body)

#Testes pra caso o post ser invalido
class ContactInvalidPost(TestCase):
    def setUp(self):
        self.resp = self.client.post('/contato/', {})

    def test_post(self):
        self.assertEqual(200, self.resp.status_code)
    
    def test_template(self):
        self.assertTemplateUsed( self.resp, 'contact/contact_form.html')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, ContactForm)
    
    def test_form_has_error(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)

#Testes pra mensagem de sucesso
class ContactSuccessMessage(TestCase):
    def test_message(self):
        data = dict(name="L.O.V.S.", phone="(53)91234-5678", email="foxyoxy87@gmail.com", message="Boa noite, como me inscrevo?")
        resp = self.client.post('/contato/', data, follow=True)
        self.assertContains(resp, 'Mensagem enviada com sucesso!')