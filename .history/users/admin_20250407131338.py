from django.contrib import admin


from users.models import Profile, Country

from django.contrib.auth.models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group




    def get_search_results(self, request, queryset, search_term):
        queryset, may_have_duplicates = super().get_search_results(
            request, queryset, search_term,
        )
        try:
            search_term_as_int = int(search_term)
        except ValueError:
            pass
        else:
            queryset |= self.model.objects.filter(phone_number=search_term_as_int)
        return queryset, may_have_duplicates


admin.site.unregister(Group)
admin.site.register(Country)
admin.site.register(User)
# admin.site.register(Site)

#@admin.register(Country)
#class CountryAdmin(admin.ModelAdmin):
    #list_display = ['name', 'is_active']
    
    
   