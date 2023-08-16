from methodism import custom_response as cr

""" Method Names Getter """

from dashboard.v1.servis.file import file_view, file_add, file_delete, file_change
from dashboard.v1.servis.patient import patient_view, patient_add, patient_change, patient_delete
from dashboard.v1.servis.diagnoz import diagnoz_view, diagnoz_add, diagnoz_change, diagnoz_delete
from dashboard.v1.servis.retseps import retsep_view, retsep_change, retsep_add, retsep_delete
from sayt.v1.servis.contact import contact_add, contact_view, contact_change,contact_delete

unusable_method = cr(True, data=dir())


def method_names(requests, params):
    datas = []
    for i in unusable_method.get('data', []):
        if '__' not in i and i != 'cr':
            datas.append(i.replace('_', '.'))

    unusable_method.update({'data': datas})
    return unusable_method
