from django.db import models
from django.utils.translation import gettext_lazy as _


class News(models.Model):
    title_en = models.CharField(_('Title (English)'), max_length=300)
    title_ar = models.CharField(_('Title (Arabic)'), max_length=300)
    title_ku = models.CharField(_('Title (Kurdish)'), max_length=300)

    excerpt_en = models.TextField(_('Excerpt (English)'))
    excerpt_ar = models.TextField(_('Excerpt (Arabic)'))
    excerpt_ku = models.TextField(_('Excerpt (Kurdish)'))

    content_en = models.TextField(_('Content (English)'), blank=True)
    content_ar = models.TextField(_('Content (Arabic)'), blank=True)
    content_ku = models.TextField(_('Content (Kurdish)'), blank=True)

    tag_en = models.CharField(_('Tag (English)'), max_length=100)
    tag_ar = models.CharField(_('Tag (Arabic)'), max_length=100)
    tag_ku = models.CharField(_('Tag (Kurdish)'), max_length=100)

    image = models.ImageField(_('Image'), upload_to='news/', blank=True)
    published_date = models.DateField(_('Published Date'))
    is_published = models.BooleanField(_('Published'), default=True)
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')
        ordering = ['-published_date']

    def __str__(self):
        return self.title_en


class Partner(models.Model):
    name = models.CharField(_('Name'), max_length=200)
    logo = models.ImageField(_('Logo'), upload_to='partners/')
    website = models.URLField(_('Website'), blank=True)
    order = models.PositiveIntegerField(_('Order'), default=0)

    class Meta:
        verbose_name = _('Partner')
        verbose_name_plural = _('Partners')
        ordering = ['order']

    def __str__(self):
        return self.name


class GalleryImage(models.Model):
    caption_en = models.CharField(_('Caption (English)'), max_length=300)
    caption_ar = models.CharField(_('Caption (Arabic)'), max_length=300)
    caption_ku = models.CharField(_('Caption (Kurdish)'), max_length=300)

    image = models.ImageField(_('Image'), upload_to='gallery/')
    order = models.PositiveIntegerField(_('Order'), default=0)

    class Meta:
        verbose_name = _('Gallery Image')
        verbose_name_plural = _('Gallery Images')
        ordering = ['order']

    def __str__(self):
        return self.caption_en


class Career(models.Model):
    class Status(models.TextChoices):
        OPEN = 'open', _('Open')
        CLOSED = 'closed', _('Closed')

    title_en = models.CharField(_('Title (English)'), max_length=300)
    title_ar = models.CharField(_('Title (Arabic)'), max_length=300)
    title_ku = models.CharField(_('Title (Kurdish)'), max_length=300)

    location_en = models.CharField(_('Location (English)'), max_length=200)
    location_ar = models.CharField(_('Location (Arabic)'), max_length=200)
    location_ku = models.CharField(_('Location (Kurdish)'), max_length=200)

    type_en = models.CharField(_('Type (English)'), max_length=100, default='Full-time')
    type_ar = models.CharField(_('Type (Arabic)'), max_length=100, default='دوام كامل')
    type_ku = models.CharField(_('Type (Kurdish)'), max_length=100, default='تەواو وەقت')

    status = models.CharField(_('Status'), max_length=10, choices=Status.choices, default=Status.OPEN)
    closes_at = models.DateField(_('Closing Date'), blank=True, null=True)
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)

    class Meta:
        verbose_name = _('Career')
        verbose_name_plural = _('Careers')
        ordering = ['-created_at']

    def __str__(self):
        return self.title_en


class JobApplication(models.Model):
    career = models.ForeignKey(Career, on_delete=models.CASCADE, related_name='applications', verbose_name=_('Career'))
    full_name = models.CharField(_('Full Name'), max_length=200)
    date_of_birth = models.DateField(_('Date of Birth'))
    city = models.CharField(_('City'), max_length=100)
    governorate = models.CharField(_('Governorate'), max_length=100)
    mobile = models.CharField(_('Mobile'), max_length=30)
    email = models.EmailField(_('Email'))
    education_level = models.CharField(_('Education Level'), max_length=100)
    cv = models.FileField(_('CV'), upload_to='cvs/')
    applied_at = models.DateTimeField(_('Applied At'), auto_now_add=True)

    class Meta:
        verbose_name = _('Job Application')
        verbose_name_plural = _('Job Applications')
        ordering = ['-applied_at']

    def __str__(self):
        return f"{self.full_name} - {self.career.title_en}"
