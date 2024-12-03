from django.test import TestCase
from datetime import datetime
from contact.models import Contact
from django.core import mail

#Entry inicial
class ContactModelTest(TestCase):
    def setUp(self):
        self.obj = Contact.objects.create(name="L.O.V.S.", phone="(53)91234-5678", email="foxyoxy87@gmail.com", message="Boa noite, como me inscrevo?")

    def test_create(self):
        self.assertTrue(Contact.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('foxyoxy87@gmail.com', str(self.obj))

    def test_replied_default_False(self):
        self.assertEqual(False, self.obj.reply_check)

    def test_blank_fields(self):
        contents = [
            'phone',
            'response',
            'reply_created_at'
        ]
        for expected in contents:
            with self.subTest():
                field = self.obj._meta.get_field('{}'.format(expected))
                self.assertTrue(field.blank)

class ContactModelReplyTest(TestCase):
    def setUp(self):
        self.obj = Contact.objects.create(name="L.O.V.S.", phone="(53)91234-5678", email="foxyoxy87@gmail.com", message="Boa noite, como me inscrevo?")

    def test_send_contact_email(self):
        self.obj.response = "Preencha o formulário na página de inscrição."
        self.obj.save()
        self.assertEqual(1, len(mail.outbox))