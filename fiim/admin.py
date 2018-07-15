from django.contrib import admin
from fiim.models import (
    Region,
    Official,
    Document,
    DocumentType,
    Partner
)

admin.site.register(Official)
admin.site.register(Region)
admin.site.register(Document)
admin.site.register(Partner)
admin.site.register(DocumentType)
