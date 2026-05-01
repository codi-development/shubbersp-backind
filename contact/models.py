from django.db import models
from django.utils.translation import gettext_lazy as _


class ContactMessage(models.Model):
    class Source(models.TextChoices):
        SOCIAL = 'social', _('Social Media')
        REFERRAL = 'referral', _('Referral')
        WEBSITE = 'website', _('Website')
        OTHER = 'other', _('Other')

    full_name = models.CharField(_('Full Name'), max_length=200)
    email = models.EmailField(_('Email'))
    phone = models.CharField(_('Phone'), max_length=30, blank=True)
    message = models.TextField(_('Message'))
    source = models.CharField(_('Source'), max_length=20, choices=Source.choices, blank=True)
    is_read = models.BooleanField(_('Read'), default=False)
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)

    class Meta:
        verbose_name = _('Contact Message')
        verbose_name_plural = _('Contact Messages')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.full_name} — {self.created_at:%Y-%m-%d %H:%M}"
