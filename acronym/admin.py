from django.contrib import admin

from .models import Acronym

# Register your models here.


class AcronymAdmin(admin.ModelAdmin):
    list_display = ('short_text','long_text','pub_date',
            'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['short_text', 'long_text']


admin.site.register(Acronym, AcronymAdmin)
    
