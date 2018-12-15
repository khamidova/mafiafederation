from django.db import models
from django.core.validators import RegexValidator
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
    document = models.ForeignKey(to="fiim.Document", on_delete=models.PROTECT, null=True, blank=True)
    published = models.BooleanField(default=False)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    email = models.EmailField(blank=True)
    vkontakte = models.URLField(blank=True)
    facebook = models.URLField(blank=True)

    def __str__(self):
        return f'{self.name} ({self.position})'


def document_type_path(instance, filename):
    return f"documents/{instance.type.code}/{filename}"


class Document(models.Model):
    type = models.ForeignKey('DocumentType', on_delete=models.PROTECT, related_name='documents')
    pdf = models.FileField(upload_to=document_type_path)
    created_at = models.DateField()
    title = models.CharField(max_length=300)
    content = RichTextField(blank=True, null=True)
    published = models.BooleanField(default=True)

    participant = models.ManyToManyField('fiim.Official', related_name='documents', blank=True)

    def __str__(self):
        return f'{self.title} от {self.created_at:%d.%m.%Y}'

    @property
    def content_adjusted(self):
        print(self.content)
        if self.content:
            return self.content
        else:
            return '<p>Текст документа доступен в PDF формате.</p>'

class DocumentType(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, primary_key=True)
    published = models.BooleanField()
    icon = models.CharField(max_length=50, default='fa fa-file')
    sorting_desc = models.BooleanField()

    def __str__(self):
        return self.name

    def published_documents(self):
        if self.sorting_desc:
            return self.documents.filter(published=True).order_by('-created_at')
        else:
            return self.documents.filter(published=True).order_by('created_at')

class Partner(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/partners')

    def __str__(self):
        return self.name
