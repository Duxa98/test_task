from django.contrib import admin

# Register your models here.
from user_list.models import AppUser, Token

admin.site.register(AppUser)
admin.site.register(Token)
