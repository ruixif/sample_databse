from django.contrib import admin
from extra.models import *
from blocks.models import *
from functions.models import *
from django.forms import TextInput, Textarea
from django.core import urlresolvers


# Register your models here.

class SampleAdmin(admin.ModelAdmin):
#    date_hierarchy='pub_date'
    list_display = ('name', 'date_created', 'date_removed_optional','Sample_type','Class','provider_name')
    liste_filter = ('name')
    date_hierarchy = 'date_created'
    ordering = ('-date_created',)
    #filter_horizontal = ('spectrum_optional',)
    search_fields = ('name', 'sample_description_optional', 'change_log_optional','provider_name__first_name','provider_name__last_name','Class__name')
    formfield_overrides = {
	models.CharField: {'widget': TextInput(attrs={'size':'20'})},
	models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})}
    }


class SpectrumAdmin(admin.ModelAdmin):
    list_display = ('spectrum_name', 'sample','link_to_Sample',)
    def link_to_Sample(self,obj):
        #temp = spectrum.objects.get(spectrum_id=obj.id)
        #if (obj is NULL):
        #   return u'<a hayak></a>'
        #else:
        return u'<a href=http://lotus.chem.cmu.edu:80/admin/blocks/sample/%s> link </a>' % (obj.sample.id)

    link_to_Sample.allow_tags=True
    search_fields = ('spectrum_name',)

#link=urlresolvers.reverse("admin:mysite_Sample_change", args=[obj.sample.id])
#class BookAdmin(admin.ModelAdmin):
#    list_display = ('title','publisher','publication_date')
#    list_filter = ('publication_date',)
#    date_hierarchy = 'publication_date'
#    ordering = ('-publication_date',)
#    filter_horizontal = ('authors',)
#    raw_id_fields = ('publisher',)

admin.site.register(Sample,SampleAdmin)
admin.site.register(Author)
admin.site.register(Sample_Class)
admin.site.register(dewar_tray)
#admin.site.register(spectrum_data,SpectrumAdmin)
admin.site.register(spectrum,SpectrumAdmin)
admin.site.register(sample_type)




