from methodism import custom_response, error_params_unfilled, MESSAGE

from base.errors import INFORMATION
from base.formats import new_format_one, new_format_all
from sayt.models import New


def salom(requests, params):
    return custom_response({'asdasadsa'})


def xayr(requests, params):
    return custom_response(True, message='Json ishladi')


def new_add(requests, params):
    nott = "title_uz" if not "title_uz" in params else "title_ru" if not "title_ru" in params else "short_desc_uz" if not "short_desc_uz" in params else "short_desc_ru" if not "short_desc_ru" in params else "desc_uz" if not "desc_uz" in params else "desc_ru" if not "desc_ru" in params else "image" if not "image" in params else ""
    if nott:
        return custom_response(False, message=error_params_unfilled(nott))
    try:
        image = params.get('image')
        title_uz = params.get('title_uz')
        title_ru = params.get('title_ru')
        short_desc_uz = params.get('short_desc_uz')
        short_desc_ru = params.get('short_desc_ru')
        desc_uz = params.get('desc_uz')
        desc_ru = params.get('desc_ru')
    except:
        return custom_response(False, message=INFORMATION['ErrorBig'])
    new_instance = New(
        image=image,
        title_uz=title_uz,
        title_ru=title_ru,
        short_desc_uz=short_desc_uz,
        short_desc_ru=short_desc_ru,
        desc_uz=desc_uz,
        desc_ru=desc_ru,
    )
    new_instance.save()
    return custom_response(True, data=new_format_one(new_instance, lan=params.get('lan', 'uz')))


def new_view(requests, params):
    if not 'lang' in requests.POST:
        return custom_response(False, message=INFORMATION['ErrorLang'])
    if not 'id' in requests.POST:
        try:
            return custom_response(status=True,
                                   data=[new_format_all(x, requests.POST.get('lang')) for x in New.objects.all()])
        except:
            return custom_response(status=False, message=INFORMATION['NotData'])
    if "id" in requests.POST:
        try:
            return custom_response(status=True,
                                   data=new_format_one(New.objects.filter(id=requests.POST.get('id')).first(),
                                                       requests.POST.get('lang', 'uz')))
        except:
            return custom_response(status=False, message=INFORMATION['NotData'])


def new_change(requests, params):
    try:
        new = New.objects.filter(pk=requests.POST['id']).first()
    except:
        return custom_response(False, message=INFORMATION['NotData'])
    try:
        new.title_uz = requests.POST.get('title_uz', new.title_uz)
        new.title_ru = requests.POST.get('title_ru', new.title_ru)
        new.short_desc_uz = requests.POST.get('short_desc_uz', new.short_desc_uz)
        new.short_desc_ru = requests.POST.get('short_desc_ru', new.short_desc_ru)
        new.desc_uz = requests.POST.get('desc_uz', new.desc_uz)
        new.desc_ru = requests.POST.get('desc_ru', new.desc_ru)
        new.date = requests.POST.get('date', new.date)
        new.image = requests.FILES.get('image', new.image)
        new.save()
        return custom_response(True, data=new_format_one(new))
    except:
        return custom_response(False, message=INFORMATION['ErrorBig'])


def new_delete(requests, params):
    try:
        new = New.objects.filter(pk=requests.POST['id']).first().delete()
        print('sasassasas')
        return custom_response(True, message=INFORMATION['NewDelete'])
    except:
        return custom_response(False, message=INFORMATION['NewDeleteError'])
