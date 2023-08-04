from methodism import custom_response as cr

from sayt.v1.servis.news import new_add,new_change,new_view,new_delete,salom,xayr
from sayt.v1.servis.doctors import doctor_add,doctor_view,doctor_change,doctor_delete


unusable_method = cr(True, data=dir())


def method_names(requests, params):
    datas = []
    for i in unusable_method.get('data', []):
        if '__' not in i and i != 'cr':
            datas.append(i.replace('_', '.'))

    unusable_method.update({'data': datas})
    return unusable_method