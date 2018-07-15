from django.db import models
from ckeditor.fields import RichTextField


DOCUMENT_TYPES = [
    ('fiim', 'Нормативные документы'),
    ('protocol', 'Протоколы собраний'),
    ('order', 'Приказы'),
    ('sk', 'Судейский комитет'),
    ('dk', 'Дисциплинарный комитет'),
]


class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Official(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=300, default='вице-президент')
    region = models.ForeignKey('fiim.Region', on_delete=models.PROTECT)
    city = models.CharField(max_length=100)
    description = RichTextField()
    photo = models.ImageField(upload_to='images/officials', default = 'images/officials/official-no-img.jpg')
    started_at = models.DateField()
    document = models.FileField(upload_to='documents')
    published = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} ({self.position})'


class Document(models.Model):
    type = models.CharField(choices=DOCUMENT_TYPES, max_length=100)
    pdf = models.FileField()
    created_at = models.DateField()
    title = models.CharField(max_length=300)
    content = RichTextField()

    participant = models.ManyToManyField('fiim.Official', related_name='documents')

    def __str__(self):
        return self.title

class Partner(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/partners')

    def __str__(self):
        return self.name
