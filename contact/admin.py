from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject',
                    'email',
                    'read')


admin.site.register(Message, MessageAdmin)
