from methodism import custom_response, MESSAGE, error_messages, error_params_unfilled

from base.errors import INFORMATION
from base.formats import retsep_format_all, retsep_format_one
from dashboard.models import Retsep


# def retsep_view(requests, params):
#
#     if not 'id' in requests.POST:
#         try:
#             return custom_response(status=True,
#                                    data=[retsep_format_all(x, requests.POST.get('lang','uz')) for x in Retsep.objects.all()])
#         except:
#             return custom_response(status=False, message=INFORMATION['NotDataTrID'])
#     if "id" in requests.POST:
#         try:
#             return custom_response(status=True,
#                                    data=retsep_format_one(Retsep.objects.filter(id=requests.POST.get('id')).first(),
#                                                           requests.POST.get('lang','uz')))
#         except:
#             return custom_response(status=False, message=MESSAGE['NotData'])

def retsep_view(requests, params):
    post_data = requests.POST
    lang = post_data.get('lang', 'uz')

    if 'id' not in post_data:
        recipes = [retsep_format_all(x, lang) for x in Retsep.objects.all()]
        return custom_response(status=True, data=recipes) if recipes else custom_response(status=False,
                                                                                          message=INFORMATION[
                                                                                              'NotDataTrID'])

    recipe_id = post_data.get('id')
    recipe = Retsep.objects.filter(id=recipe_id).first()
    if recipe:
        return custom_response(status=True, data=retsep_format_one(recipe, lang))
    else:
        return custom_response(status=False, message=MESSAGE['NotData'])


def retsep_add(requests, params):
    if not 'name_uz' or 'name ru' is requests.POST:
        return custom_response(False, message='name_uz va  name_ru bo\'lishi majburiy')
    name_uz = requests.POST.get('name_uz')
    name_ru = requests.POST.get('name_ru')
    info_uz = requests.POST.get('info_uz', '')
    info_ru = requests.POST.get('info_ru', '')

    if name_uz and name_ru:

        retsep = Retsep(name_uz=name_uz,
                        name_ru=name_ru,
                        info_uz=info_uz,
                        info_ru=info_ru)
        retsep.save()
        return custom_response(True, data=retsep_format_one(retsep))
    else:
        return custom_response(False, error_params_unfilled('xato'))


def retsep_change(requests, params):
    try:

        retsep = Retsep.objects.filter(pk=requests.POST.get('id')).first()
        if retsep == None:
            return custom_response(False, message=INFORMATION['NotDataTrID'])
    except:
        return custom_response(False, message=MESSAGE["NotData"])
    if retsep:
        retsep.name_uz = requests.POST.get('name_uz', retsep.name_uz)
        retsep.name_ru = requests.POST.get('name_ru', retsep.name_ru)
        retsep.info_uz = requests.POST.get('info_uz', retsep.info_uz)
        retsep.info_ru = requests.POST.get('info_ru', retsep.info_ru)

        retsep.save()

        return custom_response(True, retsep_format_one(retsep))
    else:
        return custom_response(False, message=MESSAGE['UndefinedError'])


def retsep_delete(requests, params):
    try:
        retsep = Retsep.objects.filter(pk=requests.POST.get('id')).first().delete()
        return custom_response(True, message=MESSAGE['UserSuccessDeleted'])
    except:
        return custom_response(False, message=INFORMATION['NotDataTrID'])
