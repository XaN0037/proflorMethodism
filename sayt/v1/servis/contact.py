from methodism import custom_response, error_params_unfilled, MESSAGE
from base.errors import INFORMATION, error_unfilled
from base.formats import doctor_format_all, contact_format_all
from sayt.models import Contact


def contact_add(request, params):
    try:
        contact_data = {field: request.POST.get(field, '') for field in (
            'phone_mobile', 'phone_clinica', 'email',
            'adress_uz', 'adress_ru', 'adress_en',
            'instagramm', 'telegram', 'facebook',
            'twitter', 'odnoklassniki', 'youtube',
            'locatsiya'
        )}

        contact = Contact(**contact_data)
        contact.save()
        return custom_response(True, data=contact_format_all(contact))
    except:
        return custom_response(False, message=INFORMATION['ErrorBig'])


def contact_view(requests, params):
    try:
        return custom_response(status=True, data=contact_format_all(Contact.objects.all().first()))
    except:
        return custom_response(status=False, message=INFORMATION['NotData'])


def contact_change(requests, params):
    contact = Contact.objects.first()

    if not contact:
        return custom_response(False, message=INFORMATION['NotData'])

    fields_to_update = [
        'phone_mobile', 'phone_clinica', 'email', 'adress_uz', 'adress_ru', 'adress_en',
        'instagramm', 'telegram', 'facebook', 'twitter', 'odnoklassniki', 'youtube', 'locatsiya'
    ]

    for field in fields_to_update:
        setattr(contact, field, requests.POST.get(field, getattr(contact, field)))

    contact.save()

    return custom_response(True, data=contact_format_all(contact))


def contact_delete(requests, params):
    try:
        new = Contact.objects.all().first().delete()
        return custom_response(True, message=INFORMATION['Contactsdelet'])
    except:
        return custom_response(False, message=INFORMATION['Contactsdeleteerror'])