from django.contrib import admin

from .models import Message, RegExp


admin.site.register(Message)
admin.site.register(RegExp)