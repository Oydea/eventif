# from django.test import TestCase
# from django.core import mail
# from contact.forms import ContactForm

# #Testes pro carregamento da página de contato
# class ContactGet(TestCase): 
#     def setUp(self):
#         self.resp = self.client.get('/contato/')

#     def test_get(self):
#         self.assertEqual(200, self.resp.status_code)
    
#     def test_template(self):
#         self.assertTemplateUsed(
#             self.resp, 'contact/contact_form.html')
    
#     def test_html(self):
#         tags = (
#             ('<form', 1),
#             ('<input', 5),
#             ('<textarea', 1),
#             ('type="text"', 2),
#             ('type="email"', 1),
#             ('type="submit"', 1)
#         )
#         for text, count in tags:
#             with self.subTest():
#                 self.assertContains(self.resp, text, count)
    
#     def test_csrf(self):
#         self.assertContains(self.resp, 'csrfmiddlewaretoken')

# #Testes pra post válido
# class ContactPostValid(TestCase):
#     def setUp(self):
#         data = dict(name="L.O.V.S.", phone="(53)91234-5678", 
#                     email="foxyoxy87@gmail.com", message="Boa noite, como me inscrevo?")
#         self.resp = self.client.post('/contato/', data)

#     def test_post(self):
#         self.assertEqual(302, self.resp.status_code)

#     def test_send_contact_email(self):
#         self.assertEqual(1, len(mail.outbox))

# #Testes pra post inválido
# class ContactPostInvalid(TestCase):
#     def setUp(self):
#         self.resp = self.client.post('/contato/', {})

#     def test_post(self):
#         self.assertEqual(200, self.resp.status_code)
    
#     def test_template(self):
#         self.assertTemplateUsed(
#             self.resp, 'contact/contact_form.html')

#     def test_has_form(self):
#         form = self.resp.context['form']
#         self.assertIsInstance(form, ContactForm)
    
#     def test_form_has_error(self):
#         form = self.resp.context['form']
#         self.assertTrue(form.errors)

# #Testes pra mensagem de sucesso
# class ContactSuccessMessage(TestCase):
#     def test_message(self):
#         data = dict(name="L.O.V.S.", phone="(53)91234-5678", 
#                     email="foxyoxy87@gmail.com", message="Boa noite, como me inscrevo?")
#         resp = self.client.post('/contato/', data, follow=True)
#         self.assertContains(resp, 'Mensagem enviada com sucesso!')