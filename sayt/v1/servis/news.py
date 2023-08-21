from django.db import transaction
from methodism import custom_response, error_params_unfilled, MESSAGE

from base.errors import INFORMATION
from base.formats import new_format_one, new_format_all
from sayt.models import New


def new_add(request, params):
    required_fields = [
        "title", "short_desc", "desc"
    ]

    languages = ['uz', 'ru']
    print(request.POST)

    missing_fields = [
        f"{field}_{lang}" for field in required_fields for lang in languages
        if f"{field}_{lang}" not in request.POST and f"{field}_{lang}" not in request.FILES
    ]

    if missing_fields:
        return custom_response(False, message=error_params_unfilled(', '.join(missing_fields)))

    try:
        image = request.FILES.get('image', '')
        field_defaults = {
            f'{field}_{lang}': request.POST.get(f'{field}_{lang}', '') for field in required_fields for lang in
            languages
        }

        new_instance = New(image=image, **field_defaults)
        new_instance.save()

    except Exception as e:
        return custom_response(False, message=INFORMATION['ErrorBig'])

    return custom_response(True, data=new_format_one(new_instance))


def new_view(requests, params):
    if not 'lang' in requests.POST:
        return custom_response(False, message=INFORMATION['ErrorLang'])
    if not 'id' in requests.POST:
        try:
            return custom_response(status=True,
                                   data=[new_format_all(x, requests.POST.get('lang')) for x in New.objects.all().order_by('-pk')])
        except:
            return custom_response(status=False, message=INFORMATION['NotData'])
    if "id" in requests.POST:
        try:
            return custom_response(status=True,
                                   data=new_format_one(New.objects.filter(id=requests.POST.get('id')).first(),
                                                       requests.POST.get('lang', 'uz')))
        except:
            return custom_response(status=False, message=INFORMATION['NotData'])


def new_change(request, params):
    new_id = request.POST.get('id')

    try:
        new = New.objects.get(pk=new_id)
    except New.DoesNotExist:
        return custom_response(False, message=INFORMATION['NotData'])

    try:
        with transaction.atomic():
            for field in ['title', 'short_desc', 'desc']:
                for lang in ['uz', 'ru']:
                    field_key = f"{field}_{lang}"
                    setattr(new, field_key, request.POST.get(field_key, getattr(new, field_key)))

            new.date = request.POST.get('date', new.date)
            new.image = request.FILES.get('image', new.image)
            new.save()

        return custom_response(True, data=new_format_one(new))
    except Exception as e:
        return custom_response(False, message=INFORMATION['ErrorBig'])





def new_delete(requests, params):
    try:
        new = New.objects.filter(pk=requests.POST['id']).first().delete()
        return custom_response(True, message=INFORMATION['NewDelete'])
    except:
        return custom_response(False, message=INFORMATION['NewDeleteError'])
