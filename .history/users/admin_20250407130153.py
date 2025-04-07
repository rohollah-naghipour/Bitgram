from django.contrib import admin


from users.models import Profile, Country


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number']



@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'abbr', 'is_active']
    
    
   