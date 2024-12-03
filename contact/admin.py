from django.contrib import admin
from contact.models import Contact

class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'message', 'created_at', 'reply_check', 'response', 'reply_created_at']
    date_hierarchy = 'created_at'
    search_fields = ('name', 'email', 'phone', 'cpf', 'message','created_at')
    list_filter = ('created_at', 'reply_check')

admin.site.register(Contact, ContactModelAdmin)