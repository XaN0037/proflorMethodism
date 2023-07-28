from methodism import custom_response as cr









from sayt.v1.servis.news import new_add






unusable_method = cr(True, data=dir())


def method_names(requests, params):
    datas = []
    for i in unusable_method.get('data', []):
        if '__' not in i and i != 'cr':
            datas.append(i.replace('_', '.'))

    unusable_method.update({'data': datas})
    return unusable_method