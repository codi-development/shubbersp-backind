from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from unfold.admin import ModelAdmin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(ModelAdmin):
    list_display = ('display_sender', 'email', 'display_source', 'is_read', 'created_at')
    list_filter = ('is_read', 'source', 'created_at')
    search_fields = ('full_name', 'email', 'message')
    list_editable = ('is_read',)
    readonly_fields = ('full_name', 'email', 'phone', 'message', 'source', 'created_at')
    list_filter_submit = True
    list_per_page = 20
    fieldsets = (
        (_('Sender Info'), {
            'fields': ('full_name', 'email', 'phone', 'source'),
        }),
        (_('Message'), {
            'fields': ('message',),
        }),
        (_('Status'), {
            'fields': ('is_read', 'created_at'),
        }),
    )

    @admin.display(description=_('Sender'))
    def display_sender(self, obj):
        icon = '🟢' if obj.is_read else '🔴'
        return format_html('{} {}', icon, obj.full_name)

    @admin.display(description=_('Source'))
    def display_source(self, obj):
        if obj.source:
            return format_html(
                '<span style="background:#F3F4F6;color:#4B5563;padding:3px 10px;border-radius:12px;font-size:12px;font-weight:600">{}</span>',
                obj.get_source_display(),
            )
        return '—'

    def has_add_permission(self, request):
        return False
