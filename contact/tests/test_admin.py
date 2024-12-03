from django.test import TestCase
from contact.admin import ContactModelAdmin, Contact, admin


class ContactModelAdminTest(TestCase):
    def setUp(self):
        Contact.objects.create(name="L.O.V.S.", phone="(53)91234-5678", email="foxyoxy87@gmail.com", message="Boa noite, como me inscrevo?")
        self.model_admin = ContactModelAdmin(Contact, admin.site)
    
    #No momento ainda não sei que testes pôr aqui