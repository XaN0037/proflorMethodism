from methodism import custom_response, MESSAGE, error_messages, error_params_unfilled

from base.errors import INFORMATION
from base.formats import diagnoz_format_one, diagnoz_format_all
from dashboard.models import Diagnoz, Patient


# def diagnoz_view(requests, params):
#     if not 'id' in requests.POST:
#         try:
#             return custom_response(status=True, data=[diagnoz_format_all(x) for x in Diagnoz.objects.all()])
#         except:
#             return custom_response(status=False, message=INFORMATION['NotDataTrID'])
#     if "id" in requests.POST:
#         try:
#             return custom_response(status=True,
#                                    data=diagnoz_format_one(Diagnoz.objects.filter(id=requests.POST['id']).first()))
#         except:
#             return custom_response(status=False, message=INFORMATION['NotData'])


def diagnoz_view(request, params):
    if 'id' not in request.POST:
        data = [diagnoz_format_all(x) for x in Diagnoz.objects.all().order_by('-pk')]
        return custom_response(status=True, data=data) if data else custom_response(status=False,
                                                                                    message=INFORMATION['NotDataTrID'])
    else:
        diagnoz = Diagnoz.objects.filter(id=request.POST['id']).first()
        return custom_response(status=True, data=diagnoz_format_one(diagnoz)) if diagnoz else custom_response(
            status=False, message=INFORMATION['NotData'])

#
# def diagnoz_add(requests, params):
#     for i in ["patient", "diagnoz", 'date']:
#         if i not in requests.POST:
#             return custom_response(False, message=error_params_unfilled(i))
#
#     if not Patient.objects.filter(id=requests.POST['patient']).first():
#         return custom_response(False, message=INFORMATION['NotDataTrID'])
#     patient = requests.POST['patient']
#     diagnoz = requests.POST.get('diagnoz', '')
#     recommendation = requests.POST.get('recommendation', '')
#     comment = requests.POST.get('comment', '')
#     date = requests.POST.get('date', '')
#     image_one = requests.FILES.get('image_one', '')
#     image_two = requests.FILES.get('image_two', '')
#
#     if patient and diagnoz and date:
#
#         diagnoz = Diagnoz.objects.create(
#             patient_id=patient,
#             diagnoz=diagnoz,
#             recommendation=recommendation,
#             date=date,
#             comment=comment,
#             image_one=image_one,
#             image_two=image_two
#         )
#
#         return custom_response(True, data=diagnoz_format_one(diagnoz))
#     else:
#         return custom_response(False, message=MESSAGE['UndefinedError'])


def diagnoz_add(request, params):
    required_fields = ["patient", "diagnoz", "date"]

    missing_fields = [field for field in required_fields if field not in request.POST]
    if missing_fields:
        return custom_response(False, message=error_params_unfilled(missing_fields[0]))

    patient = Patient.objects.filter(id=request.POST['patient']).first().id
    if not patient:
        return custom_response(False, message=INFORMATION['NotDataTrID'])

    diagnosis_data = {
        "patient_id": patient,
        "diagnoz": request.POST['diagnoz'],
        "recommendation": request.POST.get('recommendation', ''),
        "date": request.POST['date'],
        "comment": request.POST.get('comment', ''),
        "image_one": request.FILES.get('image_one', ''),
        "image_two": request.FILES.get('image_two', '')
    }

    diagnosis = Diagnoz.objects.create(**diagnosis_data)
    return custom_response(True, data=diagnoz_format_one(diagnosis))


# def diagnoz_change(requests, params):
#     try:
#
#         diagnoz = Diagnoz.objects.filter(pk=requests.POST['id']).first()
#         if diagnoz == None:
#             return custom_response(False, message=INFORMATION['NotDataTrID'])
#     except:
#         return custom_response(False, message=INFORMATION['NotDataTrID'])
#
#     if diagnoz:
#         diagnoz.diagnoz = requests.POST.get('diagnoz', diagnoz.diagnoz)
#         diagnoz.recommendation = requests.POST.get('recommendation', diagnoz.recommendation)
#         diagnoz.comment = requests.POST.get('comment', diagnoz.comment)
#         diagnoz.image_one = requests.FILES.get('image_one', diagnoz.image_one)
#         diagnoz.image_two = requests.FILES.get('image_two', diagnoz.image_two)
#
#         diagnoz.save()
#
#         return custom_response(True, diagnoz_format_one(diagnoz))
#     else:
#         return custom_response(False, message=MESSAGE['UndefinedError'])




def diagnoz_change(requests, params):
    diagnosis_id = requests.POST.get('id')
    if not diagnosis_id:
        return custom_response(False, message=INFORMATION['NotDataTrID'])

    diagnosis = Diagnoz.objects.filter(pk=diagnosis_id).first()
    if not diagnosis:
        return custom_response(False, message=INFORMATION['NotDataTrID'])

    diagnosis_fields = ['diagnoz', 'recommendation', 'comment']
    for field in diagnosis_fields:
        setattr(diagnosis, field, requests.POST.get(field, getattr(diagnosis, field)))

    image_fields = ['image_one', 'image_two']
    for field in image_fields:
        setattr(diagnosis, field, requests.FILES.get(field, getattr(diagnosis, field)))

    diagnosis.save()
    return custom_response(True, diagnoz_format_one(diagnosis))




def diagnoz_delete(requests, params):
    try:
        diagnoz = Diagnoz.objects.filter(pk=requests.POST['id']).first().delete()
        return custom_response(True, message="Diagnoz O'chirildi")
    except:
        return custom_response(False, message=INFORMATION['NotDataTrID'])
