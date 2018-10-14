from django.contrib import admin
from fiim.models import (
    Region,
    Official,
    Document,
    DocumentType,
    Partner
)


class DocumentAdmin(admin.ModelAdmin):
    filter_horizontal = ('participant',)


admin.site.register(Official)
admin.site.register(Region)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Partner)
admin.site.register(DocumentType)
