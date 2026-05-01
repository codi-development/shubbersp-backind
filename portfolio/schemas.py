from ninja import Schema
from datetime import date


class NewsOut(Schema):
    id: int
    title: str
    excerpt: str
    content: str
    tag: str
    image: str | None
    published_date: date


class PartnerOut(Schema):
    id: int
    name: str
    logo: str
    website: str


class GalleryOut(Schema):
    id: int
    caption: str
    image: str


class CareerOut(Schema):
    id: int
    title: str
    location: str
    type: str
    status: str
    closes_at: date | None


class JobApplicationIn(Schema):
    career_id: int
    full_name: str
    date_of_birth: date
    city: str
    governorate: str
    mobile: str
    email: str
    education_level: str
