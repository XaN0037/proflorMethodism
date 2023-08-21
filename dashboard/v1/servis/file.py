from methodism import custom_response, MESSAGE, error_messages, error_params_unfilled

from base.errors import INFORMATION
from base.formats import file_format
from dashboard.models import Files, Patient


def file_view(requests, params):
    if not 'id' in requests.POST:
        try:
            return custom_response(status=True, data=[file_format(x) for x in Files.objects.all().order_by('-pk')])
        except:
            return custom_response(status=False, message=INFORMATION['NotDataTrID'])
    if "id" in requests.POST:
        try:
            return custom_response(status=True,
                                   data=file_format(Files.objects.filter(id=requests.POST.get('id')).first()))
        except:
            return custom_response(status=False, message=MESSAGE['NotData'])


def file_add(requests, params):

    missing_param = next(
        (param for param in ["file", "patient"] if param not in requests.FILES and param not in requests.POST), None)
    if missing_param:
        return custom_response(False, message=error_params_unfilled(missing_param))

    patient_id = requests.POST.get('patient')
    if not Patient.objects.filter(id=patient_id).exists():
        return custom_response(False, message=INFORMATION['NotDataTrID'])

    try:
        file = Files.objects.create(patient_id=patient_id, file=requests.FILES['file'])
        return custom_response(True, data=file_format(file))
    except Exception:
        return custom_response(False, message=MESSAGE['UndefinedError'])


def file_change(requests, params):
    file_id = requests.POST.get('id')
    file = Files.objects.filter(id=file_id).first()

    if not file:
        return custom_response(False, message=INFORMATION['NotDataTrID'])

    try:
        file.file = requests.FILES.get('file', file.file)
        file.save()

        return custom_response(True, file_format(file))
    except Exception:
        return custom_response(False, message=MESSAGE['UndefinedError'])


def file_delete(requests, params):
    try:
        file = Files.objects.filter(pk=requests.POST.get('id')).first().delete()
        return custom_response(True, message="FIle O'chirildi")
    except:
        return custom_response(False, message=INFORMATION['NotDataTrID'])
