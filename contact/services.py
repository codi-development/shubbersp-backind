import logging

from django.conf import settings
from django.core.mail import send_mail

logger = logging.getLogger(__name__)


def send_contact_notification(message):
    recipient = settings.CONTACT_EMAIL
    if not recipient:
        logger.warning("CONTACT_EMAIL not configured, skipping email notification.")
        return

    subject = f"New Contact Message from {message.full_name}"
    body = (
        f"Name: {message.full_name}\n"
        f"Email: {message.email}\n"
        f"Phone: {message.phone}\n"
        f"Source: {message.get_source_display()}\n\n"
        f"Message:\n{message.message}\n"
    )

    try:
        send_mail(
            subject=subject,
            message=body,
            from_email=settings.EMAIL_HOST_USER or None,
            recipient_list=[recipient],
            fail_silently=False,
        )
    except Exception:
        logger.exception("Failed to send contact notification email.")
