from django.contrib import admin

# Register your models here.
from user_list.models import AppUser

admin.site.register(AppUser)
