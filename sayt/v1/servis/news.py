from methodism import custom_response, error_params_unfilled

from base.formats import new_format_one
from sayt.models import New


def new_add(requests, params):
    nott = "title_uz" if not "title_uz" in requests.POST else "title_ru" if not "title_ru" in requests.POST else "short_desc_uz" if not "short_desc_uz" in requests.POST else "short_desc_ru" if not "short_desc_ru" in requests.POST else "desc_uz" if not "desc_uz" in requests.POST else "desc_ru" if not "desc_ru" in requests.POST else "image" if not "image" in requests.FILES else ""
    if nott:
        return custom_response(False, message=error_params_unfilled(nott))
    try:
        image = requests.FILES.get('image')
        title_uz = requests.POST.get('title_uz')
        title_ru = requests.POST.get('title_ru')
        short_desc_uz = requests.POST.get('short_desc_uz')
        short_desc_ru = requests.POST.get('short_desc_ru')
        desc_uz = requests.POST.get('desc_uz')
        desc_ru = requests.POST.get('desc_ru')
    except:
        return custom_response(False, message=error_params_unfilled("noma'lum xatolik"))
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
    return custom_response(True, data=new_format_one(new_instance, lan=requests.POST.get('lan', 'uz')))
