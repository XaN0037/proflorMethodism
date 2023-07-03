from methodism import custom_response, MESSAGE, error_messages, error_params_unfilled

from base.formats import retsep_format_all, retsep_format_one
from dashboard.models import Retsep


def retsep_view(requests, params):
    if not 'id' in params:
        try:
            return custom_response(status=True, data=[retsep_format_all(x) for x in Retsep.objects.all()])
        except:
            return custom_response(status=False, message=MESSAGE['NotData'])
    if "id" in params:
        try:
            return custom_response(status=True,
                                   data=retsep_format_one(Retsep.objects.filter(id=params['id']).first()))
        except:
            return custom_response(status=False, message=MESSAGE['NotData'])


def retsep_add(requests, params):
    nott = 'name' if not 'name' in params else 'info' if not 'info' in params else ""

    if nott:
        return custom_response(False, message=error_params_unfilled(nott))
    name = params['name']
    info = params['info']

    if name and info:

        retsep = Retsep(name=name, info=info)
        retsep.save()
        return custom_response(True, data=retsep_format_one(retsep))
    else:
        return custom_response(False, error_params_unfilled('xato'))

def retsep_change(requests, params):
    try:

        retsep = Retsep.objects.filter(pk=params['id']).first()
    except:
        return custom_response(False, message=MESSAGE["NotData"])
    if retsep:
        retsep.name = params.get('name', retsep.name)
        retsep.info = params.get('info', retsep.info)

        retsep.save()

        return custom_response(True, retsep_format_one(retsep))
    else:
        return custom_response(False, message=MESSAGE['UndefinedError'])

def retsep_delete(requests, params):
    try:
        retsep = Retsep.objects.filter(pk=params['id']).first().delete()
        return custom_response(True, message=MESSAGE['UserSuccessDeleted'])
    except:
        return custom_response(False, message=MESSAGE['UserDeleted'])
