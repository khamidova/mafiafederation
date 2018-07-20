from django.db import models
from ckeditor.fields import RichTextField


class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Official(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=300, default='Вице-президент')
    region = models.ForeignKey('fiim.Region', on_delete=models.PROTECT)
    city = models.CharField(max_length=100)
    description = RichTextField()
    photo = models.ImageField(upload_to='images/officials', default = 'images/officials/official-no-img.jpg')
    started_at = models.DateField()
    document = models.ForeignKey(to="fiim.Document", on_delete=models.PROTECT)
    published = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} ({self.position})'

def document_type_path(instance, filename):
    return "documents/{}".format(instance.type.code)

class Document(models.Model):
    type = models.ForeignKey('DocumentType', on_delete=models.PROTECT, related_name='documents')
    pdf = models.FileField(upload_to=document_type_path)
    created_at = models.DateField()
    title = models.CharField(max_length=300)
    content = RichTextField()
    published = models.BooleanField(default=True)

    participant = models.ManyToManyField('fiim.Official', related_name='documents')

    def __str__(self):
        return self.title

class DocumentType(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, primary_key=True)
    published = models.BooleanField()
    icon = models.CharField(max_length=50, default='fa fa-file')

    def __str__(self):
        return self.name

    def published_documents(self):
        return self.documents.filter(published=True).order_by('created_at')

class Partner(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/partners')

    def __str__(self):
        return self.name
