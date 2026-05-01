from ninja import Router, UploadedFile, File
from django.shortcuts import get_object_or_404

from .models import News, Partner, GalleryImage, Career, JobApplication
from .schemas import NewsOut, PartnerOut, GalleryOut, CareerOut, JobApplicationIn

router = Router()

LANG_FIELDS = {'en', 'ar', 'ku'}


def _get_lang(request) -> str:
    lang = request.GET.get('lang', 'en')
    return lang if lang in LANG_FIELDS else 'en'


def _localize_news(news, lang) -> dict:
    return {
        'id': news.id,
        'title': getattr(news, f'title_{lang}'),
        'excerpt': getattr(news, f'excerpt_{lang}'),
        'content': getattr(news, f'content_{lang}'),
        'tag': getattr(news, f'tag_{lang}'),
        'image': news.image.url if news.image else None,
        'published_date': news.published_date,
    }


def _localize_gallery(img, lang) -> dict:
    return {
        'id': img.id,
        'caption': getattr(img, f'caption_{lang}'),
        'image': img.image.url if img.image else '',
    }


def _localize_career(career, lang) -> dict:
    return {
        'id': career.id,
        'title': getattr(career, f'title_{lang}'),
        'location': getattr(career, f'location_{lang}'),
        'type': getattr(career, f'type_{lang}'),
        'status': career.status,
        'closes_at': career.closes_at,
    }


@router.get('/news', response=list[NewsOut])
def list_news(request):
    lang = _get_lang(request)
    return [_localize_news(n, lang) for n in News.objects.filter(is_published=True)]


@router.get('/news/{news_id}', response=NewsOut)
def get_news(request, news_id: int):
    lang = _get_lang(request)
    news = get_object_or_404(News, id=news_id, is_published=True)
    return _localize_news(news, lang)


@router.get('/partners', response=list[PartnerOut])
def list_partners(request):
    return [
        {
            'id': p.id,
            'name': p.name,
            'logo': p.logo.url if p.logo else '',
            'website': p.website,
        }
        for p in Partner.objects.all()
    ]


@router.get('/gallery', response=list[GalleryOut])
def list_gallery(request):
    lang = _get_lang(request)
    return [_localize_gallery(img, lang) for img in GalleryImage.objects.all()]


@router.get('/careers', response=list[CareerOut])
def list_careers(request):
    lang = _get_lang(request)
    return [_localize_career(c, lang) for c in Career.objects.all()]


@router.get('/careers/{career_id}', response=CareerOut)
def get_career(request, career_id: int):
    lang = _get_lang(request)
    career = get_object_or_404(Career, id=career_id)
    return _localize_career(career, lang)


@router.post('/careers/{career_id}/apply')
def apply_to_job(request, career_id: int, data: JobApplicationIn, cv: UploadedFile = File(...)):
    career = get_object_or_404(Career, id=career_id, status='open')
    application = JobApplication.objects.create(
        career=career,
        full_name=data.full_name,
        date_of_birth=data.date_of_birth,
        city=data.city,
        governorate=data.governorate,
        mobile=data.mobile,
        email=data.email,
        education_level=data.education_level,
        cv=cv,
    )
    return {'success': True, 'id': application.id}
