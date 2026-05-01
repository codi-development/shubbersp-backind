from .models import ContactMessage


def unread_count(request):
    count = ContactMessage.objects.filter(is_read=False).count()
    return str(count) if count > 0 else ""
