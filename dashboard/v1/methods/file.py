from methodism import custom_response, MESSAGE, error_messages, error_params_unfilled

from base.formats import file_format
from dashboard.models import Files, Patient


def file_view(requests, params):
    if not 'id' in params:
        try:
            return custom_response(status=True, data=[file_format(x) for x in Files.objects.all()])
        except:
            return custom_response(status=False, message=MESSAGE['NotData'])
    if "id" in params:
        try:
            return custom_response(status=True,
                                   data=file_format(Files.objects.filter(id=params['id']).first()))
        except:
            return custom_response(status=False, message=MESSAGE['NotData'])


#
def file_add(requests, params):
    nott = 'patient' if not 'patient' in requests.POST else 'file' if not 'info' in requests.POST else ""
    if nott:
        return custom_response(False, message=error_params_unfilled(nott))
    if not Patient.objects.filter(id=requests.POST.get('patient')).first():
        return custom_response(False, message="Bu ID da patient yo")
    patient = requests.POST.get('patient')
    try:
        file = Files(patient_id=patient, file=requests.FILES.get('file'))
        file.save()
        return custom_response(True, data=file_format(file))
    except:
        return custom_response(False, message="File ni yuklab bo'lmadi")

# patient = params['patient']
#     # diagnoz = params['diagnoz']
#     # recommendation = params['recommendation']
#     # comment = params['comment']
#     # date = params['date']
#     # image_one = params.get('image_one', '')
#     # image_two = params.get('image_two', '')
#     #
#     # if patient and diagnoz and recommendation and comment and date:
#
#     diagnoz = Diagnoz.objects.create(
#         patient_id=patient,
#         diagnoz=diagnoz,
#         recommendation=recommendation,
#         date=date,
#         comment=comment,
#         image_one=image_one,
#         image_two=image_two
#     )
#
#     return custom_response(True, data=diagnoz_format_one(diagnoz))
# else:
#     return custom_response(False, error_params_unfilled('xato'))

#
# #
# #
# def diagnoz_change(requests, params):
#     try:
#
#         diagnoz = Diagnoz.objects.filter(pk=params['id']).first()
#     except:
#         return custom_response(False, message=MESSAGE["NotData"])
#
#     if diagnoz:
#         diagnoz.patient_id = params.get('patient', diagnoz.patient_id)
#         if not Patient.objects.filter(id=diagnoz.patient_id).first():
#             return custom_response(False, message="patient yo")
#         diagnoz.diagnoz = params.get('diagnoz', diagnoz.diagnoz)
#         diagnoz.recommendation = params.get('recommendation', diagnoz.recommendation)
#         diagnoz.comment = params.get('comment', diagnoz.comment)
#         diagnoz.date = params.get('date', diagnoz.date)
#         diagnoz.image_one = params.get('image_one', diagnoz.image_one)
#         diagnoz.image_two = params.get('image_two', diagnoz.image_two)
#
#         diagnoz.save()
#
#         return custom_response(True, diagnoz_format_one(diagnoz))
#     else:
#         return custom_response(False, message=MESSAGE['UndefinedError'])
#
# def diagnoz_delete(requests, params):
#     try:
#         diagnoz = Diagnoz.objects.filter(pk=params['id']).first().delete()
#         return custom_response(True, message="Diagnoz O'chirildi")
#     except:
#         return custom_response(False, message=MESSAGE['NotData'])
