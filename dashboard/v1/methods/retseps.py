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
