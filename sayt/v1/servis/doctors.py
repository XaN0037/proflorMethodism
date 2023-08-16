from methodism import custom_response, error_params_unfilled, MESSAGE
from base.errors import INFORMATION, error_unfilled
from base.formats import doctor_format_all
from sayt.models import Doctor


# def doctor_add(requests, params):
#     if "image" not in requests.FILES and 'name_uz' not in requests.POST:
#         return custom_response(False, message=error_unfilled("image va name_uz"))
#     try:
#         name_uz = requests.POST.get('name_uz', '')
#         first_name_uz = requests.POST.get('first_name_uz', '')
#         middle_name_uz = requests.POST.get('middle_name_uz', '')
#         name_ru = requests.POST.get('name_ru', '')
#         first_name_ru = requests.POST.get('first_name_ru', '')
#         middle_name_ru = requests.POST.get('middle_name_ru', '')
#         name_en = requests.POST.get('name_en', '')
#         first_name_en = requests.POST.get('first_name_en', '')
#         middle_name_en = requests.POST.get('middle_name_en', '')
#         specialty_uz = requests.POST.get('specialty_uz', '')
#         specialty_ru = requests.POST.get('specialty_ru', '')
#         specialty_en = requests.POST.get('specialty_en', '')
#         about_doctor_uz = requests.POST.get('about_doctor_uz', '')
#         about_doctor_ru = requests.POST.get('about_doctor_ru', '')
#         about_doctor_en = requests.POST.get('about_doctor_en', '')
#         phone = requests.POST.get('phone', '')
#         email = requests.POST.get('email', '')
#         instagramm = requests.POST.get('instagramm', '')
#         telegram = requests.POST.get('telegram', '')
#         facebook = requests.POST.get('facebook', '')
#         twitter = requests.POST.get('twitter', '')
#         odnoklassniki = requests.POST.get('odnoklassniki', '')
#         image = requests.FILES.get('image')
#     except:
#         return custom_response(False, message=INFORMATION['ErrorBig'])
#     try:
#         doctor = Doctor(
#             name_uz=name_uz,
#             first_name_uz=first_name_uz,
#             middle_name_uz=middle_name_uz,
#             name_ru=name_ru,
#             first_name_ru=first_name_ru,
#             middle_name_ru=middle_name_ru,
#             name_en=name_en,
#             first_name_en=first_name_en,
#             middle_name_en=middle_name_en,
#             specialty_uz=specialty_uz,
#             specialty_ru=specialty_ru,
#             specialty_en=specialty_en,
#             about_doctor_uz=about_doctor_uz,
#             about_doctor_ru=about_doctor_ru,
#             about_doctor_en=about_doctor_en,
#             phone=phone,
#             email=email,
#             instagramm=instagramm,
#             telegram=telegram,
#             facebook=facebook,
#             twitter=twitter,
#             odnoklassniki=odnoklassniki,
#             image=image,
#         )
#         doctor.save()
#         return custom_response(True, data=doctor_format_all(doctor))
#     except:
#         custom_response(False, INFORMATION['ErrorBig'])



def doctor_add(requests, params):
    required_fields = ['image', 'name_uz']
    if not all(field in requests.FILES or field in requests.POST for field in required_fields):
        return custom_response(False, message=error_unfilled(", ".join(required_fields)))

    try:
        doctor_data = {
            'name_uz': requests.POST.get('name_uz', ''),
            'first_name_en': requests.POST.get('first_name_en', ''),
            'middle_name_uz': requests.POST.get('middle_name_uz', ''),
            'name_ru': requests.POST.get('name_ru', ''),
            'first_name_ru': requests.POST.get('first_name_ru', ''),
            'middle_name_ru': requests.POST.get('middle_name_ru', ''),
            'name_en': requests.POST.get('name_en', ''),
            'first_name_en': requests.POST.get('first_name_en', ''),
            'middle_name_en': requests.POST.get('middle_name_en', ''),
            'specialty_uz': requests.POST.get('specialty_uz', ''),
            'specialty_ru': requests.POST.get('specialty_ru', ''),
            'specialty_en': requests.POST.get('specialty_en', ''),
            'about_doctor_uz': requests.POST.get('about_doctor_uz', ''),
            'about_doctor_ru': requests.POST.get('about_doctor_ru', ''),
            'about_doctor_en': requests.POST.get('about_doctor_en', ''),
            'phone': requests.POST.get('phone', ''),
            'email': requests.POST.get('email', ''),
            'instagramm': requests.POST.get('instagramm', ''),
            'telegram': requests.POST.get('telegram', ''),
            'facebook': requests.POST.get('facebook', ''),
            'twitter': requests.POST.get('twitter', ''),
            'odnoklassniki': requests.POST.get('odnoklassniki', ''),
            'image': requests.FILES.get('image'),
        }
    except:
        return custom_response(False, message=INFORMATION['ErrorBig'])

    try:
        doctor = Doctor(**doctor_data)
        doctor.save()
        return custom_response(True, data=doctor_format_all(doctor))
    except:
        return custom_response(False, message=INFORMATION['ErrorBig'])


def doctor_view(requests, params):
    if not 'lang' in requests.POST:
        return custom_response(False, message=INFORMATION['ErrorLang'])
    if not 'id' in requests.POST:
        try:
            return custom_response(status=True,
                                   data=[doctor_format_all(x, requests.POST.get('lang', 'uz')) for x in
                                         Doctor.objects.all()])
        except:
            return custom_response(status=False, message=INFORMATION['NotData'])
    if "id" in requests.POST:
        try:
            return custom_response(status=True,
                                   data=doctor_format_all(Doctor.objects.filter(id=requests.POST.get('id')).first(),
                                                          requests.POST.get('lang', 'uz')))
        except:
            return custom_response(status=False, message=INFORMATION['NotData'])


def doctor_change(requests, params):
    try:
        doctor = Doctor.objects.filter(pk=requests.POST['id']).first()
    except:
        return custom_response(False, message=INFORMATION['NotData'])
    try:
        doctor.name_uz = requests.POST.get('name_uz', doctor.name_uz)
        doctor.first_name_uz = requests.POST.get('first_name_uz', doctor.first_name_uz)
        doctor.middle_name_uz = requests.POST.get('middle_name_uz', doctor.middle_name_uz)
        doctor.name_ru = requests.POST.get('name_ru', doctor.name_ru)
        doctor.first_name_ru = requests.POST.get('first_name_ru', doctor.first_name_ru)
        doctor.middle_name_ru = requests.POST.get('middle_name_ru', doctor.middle_name_ru)
        doctor.name_en = requests.POST.get('name_en', doctor.name_en)
        doctor.first_name_en = requests.POST.get('first_name_en', doctor.first_name_en)
        doctor.middle_name_en = requests.POST.get('middle_name_en', doctor.middle_name_en)
        doctor.specialty_uz = requests.POST.get('specialty_uz', doctor.specialty_uz)
        doctor.specialty_ru = requests.POST.get('specialty_ru', doctor.specialty_ru)
        doctor.specialty_en = requests.POST.get('specialty_en', doctor.specialty_en)
        doctor.about_doctor_uz = requests.POST.get('about_doctor_uz', doctor.about_doctor_uz)
        doctor.about_doctor_ru = requests.POST.get('about_doctor_ru', doctor.about_doctor_ru)
        doctor.about_doctor_en = requests.POST.get('about_doctor_en', doctor.about_doctor_en)
        doctor.phone = requests.POST.get('phone', doctor.phone)
        doctor.email = requests.POST.get('email', doctor.email)
        doctor.instagramm = requests.POST.get('instagramm', doctor.instagramm)
        doctor.telegram = requests.POST.get('telegram', doctor.telegram)
        doctor.facebook = requests.POST.get('facebook', doctor.facebook)
        doctor.twitter = requests.POST.get('twitter', doctor.twitter)
        doctor.odnoklassniki = requests.POST.get('odnoklassniki', doctor.odnoklassniki)
        doctor.image = requests.FILES.get('image', doctor.image)
        doctor.save()
        return custom_response(True, data=doctor_format_all(doctor))
    except:
        return custom_response(False, message=INFORMATION['ErrorBig'])

def doctor_delete(requests, params):
    try:
        new = Doctor.objects.filter(pk=requests.POST['id']).first().delete()
        return custom_response(True, message=INFORMATION['NewDelete'])
    except:
        return custom_response(False, message=INFORMATION['NewDeleteError'])
