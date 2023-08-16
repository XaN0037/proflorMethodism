from methodism import custom_response, MESSAGE, error_messages, error_params_unfilled

from base.errors import INFORMATION
from base.formats import file_format
from dashboard.models import Files, Patient


def file_view(requests, params):
    if not 'id' in requests.POST:
        try:
            return custom_response(status=True, data=[file_format(x) for x in Files.objects.all()])
        except:
            return custom_response(status=False, message=INFORMATION['NotDataTrID'])
    if "id" in requests.POST:
        try:
            return custom_response(status=True,
                                   data=file_format(Files.objects.filter(id=requests.POST.get('id')).first()))
        except:
            return custom_response(status=False, message=MESSAGE['NotData'])


def file_add(requests, params):
    # nott = "file" if not "file" in requests.FILES else "patient" if not "patient" in requests.POST else ""
    # if nott:
    #     return custom_response(False, message=error_params_unfilled(nott))

    for i in ["file", "patient"]:
        if i not in requests.POST:
            return custom_response(False, message=error_params_unfilled(i))

    if not Patient.objects.filter(id=requests.POST.get('patient')).first():
        return custom_response(False, message=INFORMATION['NotDataTrID'])

    try:
        file = Files(patient_id=requests.POST.get('patient'), file=requests.FILES.get('file'))
        file.save()
        return custom_response(True, data=file_format(file))
    except:
        return custom_response(False, message=MESSAGE['UndefinedError'])


def file_change(requests, params):
    if not Files.objects.filter(id=requests.POST.get('id')).first():
        return custom_response(False, message=INFORMATION['NotDataTrID'])
    try:
        file = Files.objects.filter(id=requests.POST.get('id')).first()
        file.file = requests.FILES.get('file', file.file)
        file.id = requests.POST.get('id', file.id)
        file.save()

        return custom_response(True, file_format(file))
    except:
        return custom_response(False, message=MESSAGE['UndefinedError'])


def file_delete(requests, params):
    try:
        file = Files.objects.filter(pk=requests.POST.get('id')).first().delete()
        return custom_response(True, message="FIle O'chirildi")
    except:
        return custom_response(False, message=INFORMATION['NotDataTrID'])
