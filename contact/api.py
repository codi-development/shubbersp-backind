from ninja import Router

from .models import ContactMessage
from .schemas import ContactIn, ContactOut
from .services import send_contact_notification

router = Router()


@router.post('/', response=ContactOut)
def send_message(request, data: ContactIn):
    msg = ContactMessage.objects.create(
        full_name=data.full_name,
        email=data.email,
        phone=data.phone,
        message=data.message,
        source=data.source,
    )
    send_contact_notification(msg)
    return {'success': True, 'message': 'Message sent successfully.'}
