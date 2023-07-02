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

    if first_name and father_name and age and phone:

        patient = Patient(
            name=name,
            first_name=first_name,
            father_name=father_name,
            age=age,
            phone=phone,
            comment=comment
        )
        patient.save()
        print('shu joygach atogriiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
        return custom_response(True, data=patient_format_one(patient))
    else:
        return custom_response(False, error_params_unfilled('xato'))

