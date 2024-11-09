from uuid import uuid4
from pytils.translit import slugify
from django.core.paginator import Paginator


def is_htmx(request, boost_check=True):
    hx_boost = request.headers.get("Hx-Boosted")
    hx_request = request.headers.get("Hx-Request")
    if boost_check and hx_boost:
        return False

    elif boost_check and not hx_boost and hx_request:
        return True


def paginate(request, qs, limit):
    paginated_qs = Paginator(qs, limit)
    page_no = request.GET.get("page")
    return paginated_qs.get_page(page_no)



def unique_slugify(instance, slug):
    """
    Генератор уникальных SLUG для моделей, в случае существования такого SLUG.
    """
    model = instance.__class__
    unique_slug = slugify(slug)
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = f'{unique_slug}-{uuid4().hex[:8]}'
    return unique_slug