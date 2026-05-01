from ninja import Schema


class ContactIn(Schema):
    full_name: str
    email: str
    phone: str = ''
    message: str
    source: str = ''


class ContactOut(Schema):
    success: bool
    message: str
