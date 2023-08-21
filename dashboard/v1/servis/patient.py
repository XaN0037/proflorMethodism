from methodism import custom_response, MESSAGE, error_messages, error_params_unfilled

from base.errors import INFORMATION
from base.formats import patient_format_one, patient_format_all
from dashboard.models import Patient


def patient_view(requests, params):
    if not 'id' in requests.POST:
        try:
            return custom_response(status=True, data=[patient_format_all(x) for x in Patient.objects.all().order_by('-pk')])
        except:
            return custom_response(status=False, message=INFORMATION['NotDataTrID'])
    if "id" in requests.POST:
        try:
            return custom_response(status=True,
                                   data=patient_format_one(Patient.objects.filter(id=requests.POST['id']).first()))
        except:
            return custom_response(status=False, message=MESSAGE['NotData'])


def patient_add(requests, params):
    nott = 'first_name' if not 'first_name' in requests.POST else 'name' if not 'name' in requests.POST else ""

    if nott:
        return custom_response(False, message=error_params_unfilled(nott))
    name = requests.POST['name']
    first_name = requests.POST['first_name']
    father_name = requests.POST.get('father_name', '')
    age = requests.POST.get('age', '')
    phone = requests.POST.get('phone', '')
    comment = requests.POST.get('comment', '')

    if name and first_name:

        patient = Patient(
            name=name,
            first_name=first_name,
            father_name=father_name,
            age=age,
            phone=phone,
            comment=comment
        )
        patient.save()
        return custom_response(True, data=patient_format_one(patient))
    else:
        return custom_response(False, message=MESSAGE['UndefinedError'])


def patient_change(requests, params):
    try:

        patient = Patient.objects.filter(pk=requests.POST['id']).first()
        if patient == None:
            return custom_response(False, message=INFORMATION['NotDataTrID'])
    except:
        return custom_response(False, message=MESSAGE["NotData"])
    if patient:
        patient.name = requests.POST.get('name', patient.name)
        patient.first_name = requests.POST.get('first_name', patient.first_name)
        patient.father_name = requests.POST.get('father_name', patient.father_name)
        patient.age = requests.POST.get('age', patient.age)
        patient.phone = requests.POST.get('phone', patient.phone)
        patient.comment = requests.POST.get('comment', patient.comment)

        patient.save()

        return custom_response(True, patient_format_one(patient))
    else:
        return custom_response(False, message=MESSAGE['UndefinedError'])


def patient_delete(requests, params):
    try:
        patient = Patient.objects.filter(pk=requests.POST['id']).first().delete()
        return custom_response(True, message=MESSAGE['UserSuccessDeleted'])
    except:
        return custom_response(False, message=INFORMATION['NotDataTrID'])
