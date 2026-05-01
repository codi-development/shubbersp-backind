from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from unfold.admin import ModelAdmin
from .models import News, Partner, GalleryImage, Career, JobApplication


@admin.register(News)
class NewsAdmin(ModelAdmin):
    list_display = ('title_en', 'display_tag', 'published_date', 'is_published')
    list_filter = ('is_published', 'tag_en', 'published_date')
    search_fields = ('title_en', 'title_ar', 'title_ku')
    list_editable = ('is_published',)
    list_filter_submit = True
    list_per_page = 20
    fieldsets = (
        ('English', {
            'classes': ['tab'],
            'fields': ('title_en', 'excerpt_en', 'content_en', 'tag_en'),
        }),
        ('العربية', {
            'classes': ['tab'],
            'fields': ('title_ar', 'excerpt_ar', 'content_ar', 'tag_ar'),
        }),
        ('کوردی', {
            'classes': ['tab'],
            'fields': ('title_ku', 'excerpt_ku', 'content_ku', 'tag_ku'),
        }),
        (_('Media & Status'), {
            'classes': ['tab'],
            'fields': ('image', 'published_date', 'is_published'),
        }),
    )

    @admin.display(description=_('Tag'))
    def display_tag(self, obj):
        return format_html(
            '<span style="background:#FFF7ED;color:#E26314;padding:3px 10px;border-radius:12px;font-size:12px;font-weight:600">{}</span>',
            obj.tag_en,
        )


@admin.register(Partner)
class PartnerAdmin(ModelAdmin):
    list_display = ('display_logo', 'name', 'website', 'order')
    list_editable = ('order',)
    search_fields = ('name',)
    list_per_page = 20

    @admin.display(description=_('Logo'))
    def display_logo(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="height:32px;width:auto;border-radius:6px;object-fit:contain" />', obj.logo.url)
        return '—'


@admin.register(GalleryImage)
class GalleryImageAdmin(ModelAdmin):
    list_display = ('display_thumbnail', 'caption_en', 'order')
    list_editable = ('order',)
    list_per_page = 20

    @admin.display(description=_('Preview'))
    def display_thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:48px;width:72px;border-radius:8px;object-fit:cover" />', obj.image.url)
        return '—'


@admin.register(Career)
class CareerAdmin(ModelAdmin):
    list_display = ('title_en', 'location_en', 'type_en', 'status', 'closes_at')
    list_filter = ('status',)
    list_filter_submit = True
    list_per_page = 20
    fieldsets = (
        ('English', {
            'classes': ['tab'],
            'fields': ('title_en', 'location_en', 'type_en'),
        }),
        ('العربية', {
            'classes': ['tab'],
            'fields': ('title_ar', 'location_ar', 'type_ar'),
        }),
        ('کوردی', {
            'classes': ['tab'],
            'fields': ('title_ku', 'location_ku', 'type_ku'),
        }),
        (_('Status'), {
            'classes': ['tab'],
            'fields': ('status', 'closes_at'),
        }),
    )


@admin.register(JobApplication)
class JobApplicationAdmin(ModelAdmin):
    list_display = ('full_name', 'career', 'email', 'city', 'education_level', 'display_cv', 'applied_at')
    list_filter = ('career', 'city', 'education_level', 'applied_at')
    search_fields = ('full_name', 'email')
    readonly_fields = ('full_name', 'career', 'date_of_birth', 'city', 'governorate', 'mobile', 'email', 'education_level', 'cv', 'applied_at')
    list_filter_submit = True
    list_per_page = 20

    @admin.display(description=_('CV'))
    def display_cv(self, obj):
        if obj.cv:
            return format_html('<a href="{}" target="_blank" style="color:#E26314;font-weight:600">{}</a>', obj.cv.url, _('Download'))
        return '—'

    def has_add_permission(self, request):
        return False
