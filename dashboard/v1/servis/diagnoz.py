from methodism import custom_response, MESSAGE, error_messages, error_params_unfilled

from base.formats import diagnoz_format_one, diagnoz_format_all
from dashboard.models import Diagnoz, Patient


def diagnoz_view(requests, params):
    if not 'id' in params:
        try:
            return custom_response(status=True, data=[diagnoz_format_all(x) for x in Diagnoz.objects.all()])
        except:
            return custom_response(status=False, message=MESSAGE['NotData'])
    if "id" in params:
        try:
            return custom_response(status=True,
                                   data=diagnoz_format_one(Diagnoz.objects.filter(id=params['id']).first()))
        except:
            return custom_response(status=False, message=MESSAGE['NotData'])


def diagnoz_add(requests, params):
    nott = 'patient' if not 'patient' in requests.POST else 'diagnoz' if not 'diagnoz' in requests.POST else "date" if not 'date' in requests.POST else ''
    if nott:
        return custom_response(False, message=error_params_unfilled(nott))
    if not Patient.objects.filter(id=requests.POST['patient']).first():
        return custom_response(False, message=MESSAGE['NOTPATIENT'])
    patient = requests.POST['patient']
    diagnoz = requests.POST.get('diagnoz', '')
    recommendation = requests.POST.get('recommendation', '')
    comment = requests.POST.get('comment', '')
    date = requests.POST.get('date', '')
    image_one = requests.FILES.get('image_one', '')
    image_two = requests.FILES.get('image_two', '')

    if patient and diagnoz and date:

        diagnoz = Diagnoz.objects.create(
            patient_id=patient,
            diagnoz=diagnoz,
            recommendation=recommendation,
            date=date,
            comment=comment,
            image_one=image_one,
            image_two=image_two
        )

        return custom_response(True, data=diagnoz_format_one(diagnoz))
    else:
        return custom_response(False, message=MESSAGE['UndefinedError'])


def diagnoz_change(requests, params):
    try:

        diagnoz = Diagnoz.objects.filter(pk=requests.POST['id']).first()
        if diagnoz == None:
            return custom_response(False, message=MESSAGE['NotData'])
    except:
        return custom_response(False, message=MESSAGE["NotData"])

    if diagnoz:
        diagnoz.diagnoz = requests.POST.get('diagnoz', diagnoz.diagnoz)
        diagnoz.recommendation = requests.POST.get('recommendation', diagnoz.recommendation)
        diagnoz.comment = requests.POST.get('comment', diagnoz.comment)
        diagnoz.image_one = requests.FILES.get('image_one', diagnoz.image_one)
        diagnoz.image_two = requests.FILES.get('image_two', diagnoz.image_two)

        diagnoz.save()

        return custom_response(True, diagnoz_format_one(diagnoz))
    else:
        return custom_response(False, message=MESSAGE['UndefinedError'])


def diagnoz_delete(requests, params):
    try:
        diagnoz = Diagnoz.objects.filter(pk=requests.POST['id']).first().delete()
        return custom_response(True, message="Diagnoz O'chirildi")
    except:
        return custom_response(False, message=MESSAGE['NotData'])
