from methodism import custom_response, MESSAGE, error_messages, error_params_unfilled

from base.formats import patient_format_one, patient_format_all
from dashboard.models import Patient


def patient_view(requests, params):
    if not 'id' in params:
        try:
            return {'data': custom_response(status=True, data=[patient_format_all(x) for x in Patient.objects.all()])}
        except:
            return custom_response(status=False, message=MESSAGE['NotData'])
    if "id" in params:
        try:
            return {'data': custom_response(status=True,
                                            data=patient_format_one(Patient.objects.filter(id=params['id']).first()))}
        except:
            return custom_response(status=False, message=MESSAGE['NotData'])


def patient_add(requests, params):
    nott = 'first_name' if not 'first_name' in params else 'father_name' if not 'father_name' in params else "age" if not "age" in params else "phone" if not 'phone' in params else "comment" if not "comment" in params else 'name' if not 'name' in params else ""

    if nott:
        return custom_response(False, message=error_params_unfilled(nott))
    name = params['name']
    first_name = params['first_name']
    father_name = params['father_name']
    age = params['age']
    phone = params['phone']
    comment = params['comment']

    if name and first_name and father_name and age and phone and comment:

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

        patient = Patient.objects.filter(pk=params['id']).first()
    except:
        return custom_response(False, message=MESSAGE["NotData"])
    if patient:
        patient.name = params.get('name', patient.name)
        patient.first_name = params.get('first_name', patient.first_name)
        patient.father_name = params.get('father_name', patient.father_name)
        patient.age = params.get('age', patient.age)
        patient.phone = params.get('phone', patient.phone)
        patient.comment = params.get('comment', patient.comment)

        patient.save()

        return custom_response(True, patient_format_one(patient))
    else:
        return custom_response(False, message=MESSAGE['UndefinedError'])

def patient_delete(requests, params):
    try:
        patient = Patient.objects.filter(pk=params['id']).first().delete()
        return custom_response(True, message=MESSAGE['UserSuccessDeleted'])
    except:
        return custom_response(False, message=MESSAGE['UserDeleted'])
