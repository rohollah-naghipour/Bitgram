from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


from users.models import Profile, Country

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number']


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']    