from django.test import TestCase
from django.core import mail
from contact.models import Contact

#Testes pra email válido
class ContactPostValid(TestCase):
    def setUp(self):
        data = dict(name="L.O.V.S.", phone="(53)91234-5678", 
                    email="foxyoxy87@gmail.com", message="Boa noite, como me inscrevo?")
        self.client.post('/contato/', data)
        self.email = mail.outbox[0]

    def test_contact_email_subject(self):
        expect = "Entrando em contato!"
        self.assertEqual(expect, self.email.subject)
    
    def test_contact_email_from(self):
        expect = "foxyoxy87@gmail.com"
        self.assertEqual(expect, self.email.from_email)

    def test_contact_email_to(self):
        expect = ["foxyoxy87@gmail.com", "contato@eventif.com.br"]
        self.assertEqual(expect, self.email.to)

    def test_contact_email_body(self):
        contents = (
            'L.O.V.S.',
            '(53)91234-5678',
            'foxyoxy87@gmail.com',
            'Boa noite, como me inscrevo?'
        )
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)

class ContactReplyEmail(TestCase):
    def setUp(self):
        self.obj = Contact.objects.create(name="L.O.V.S.", phone="(53)91234-5678", email="foxyoxy87@gmail.com", message="Boa noite, como me inscrevo?")
        self.obj.response = "Preencha o formulário na página de inscrição."
        self.obj.save()
        self.email = mail.outbox[0]

    def test_reply_email_subject(self):
        expect = "Retorno de contato!"
        self.assertEqual(expect, self.email.subject)
    
    def test_reply_email_from(self):
        expect = "contato@eventif.com.br"
        self.assertEqual(expect, self.email.from_email)

    def test_contact_email_to(self):
        expect = ["contato@eventif.com.br", "foxyoxy87@gmail.com"]
        self.assertEqual(expect, self.email.to)

    def test_contact_email_body(self):
        contents = (
            'L.O.V.S.',
            '(53)91234-5678',
            'foxyoxy87@gmail.com',
            'Boa noite, como me inscrevo?',
            'Preencha o formulário na página de inscrição.'
        )
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)