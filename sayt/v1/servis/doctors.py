from methodism import custom_response, error_params_unfilled, MESSAGE
from base.errors import INFORMATION, error_unfilled
from base.formats import doctor_format_all
from sayt.models import Doctor


def doctor_add(requests, params):
    required_fields = ['image', 'name_en']

    if not all(field in requests.FILES or field in requests.POST for field in required_fields):
        return custom_response(False, message=error_unfilled(", ".join(required_fields)))

    doctor_data = {field: requests.POST.get(field, '') for field in (
        'name_uz', 'first_name_uz', 'middle_name_uz',
        'name_ru', 'first_name_ru', 'middle_name_ru',
        'name_en', 'first_name_en', 'middle_name_en',
        'specialty_uz', 'specialty_ru', 'specialty_en',
        'about_doctor_uz', 'about_doctor_ru', 'about_doctor_en',
        'phone', 'email', 'instagramm', 'telegram', 'facebook', 'twitter', 'odnoklassniki'
    )}
    doctor_data['image'] = requests.FILES.get('image')

    try:
        doctor = Doctor(**doctor_data)
        doctor.save()
        return custom_response(True, data=doctor_format_all(doctor))
    except Exception:
        return custom_response(False, message=INFORMATION['ErrorBig'])


def doctor_view(requests, params):
    lang = requests.POST.get('lang', 'en')
    id_param = requests.POST.get('id')

    doctors = Doctor.objects.all()

    if not id_param:
        data = [doctor_format_all(doctor, lang) for doctor in doctors]
    else:
        doctor = doctors.filter(id=id_param).first()
        if doctor:
            data = doctor_format_all(doctor, lang)
        else:
            return custom_response(status=False, message=INFORMATION['NotData'])

    return custom_response(status=True, data=data)


def doctor_change(requests, params):
    doctor_id = requests.POST.get('id')

    if not doctor_id:
        return custom_response(False, message=INFORMATION['NotData'])

    doctor = Doctor.objects.filter(pk=doctor_id).first()

    if not doctor:
        return custom_response(False, message=INFORMATION['NotData'])

    field_mapping = {'name_uz': 'name',
                     'first_name_uz': 'first_name',
                     'middle_name_uz': 'middle_name',
                     'name_ru': 'name',
                     'first_name_ru': 'first_name',
                     'middle_name_ru': 'middle_name',
                     'name_en': 'name',
                     'first_name_en': 'first_name',
                     'middle_name_en': 'middle_name',
                     'specialty_uz': 'specialty',
                     'specialty_ru': 'specialty',
                     'specialty_en': 'specialty',
                     'about_doctor_uz': 'about_doctor',
                     'about_doctor_ru': 'about_doctor',
                     'about_doctor_en': 'about_doctor',
                     'phone': 'phone',
                     'email': 'email',
                     'instagramm': 'instagramm',
                     'telegram': 'telegram',
                     'facebook': 'facebook',
                     'twitter': 'twitter',
                     'odnoklassniki': 'odnoklassniki'
                     }

    for field, attr in field_mapping.items():
        setattr(doctor, attr, requests.POST.get(field, getattr(doctor, attr)))

    doctor.image = requests.FILES.get('image', doctor.image)
    doctor.save()

    return custom_response(True, data=doctor_format_all(doctor))


def doctor_delete(request, params):
    try:
        doctor_id = request.POST.get('id')
        if doctor_id:
            Doctor.objects.filter(pk=doctor_id).delete()
            return custom_response(True, message=INFORMATION['NewDelete'])
        return custom_response(False, message=INFORMATION['NewDeleteError'])
    except Exception as e:
        return custom_response(False, message=INFORMATION['NewDeleteError'])

