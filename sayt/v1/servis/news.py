from methodism import custom_response






def new_add(requests, params):
    return custom_response(True,message='ishladi')



# def file_add(requests, params):
#     nott = "file" if not "file" in requests.FILES else "patient" if not "patient" in requests.POST else ""
#     if nott:
#         return custom_response(False, message=error_params_unfilled(nott))
#
#     if not Patient.objects.filter(id=requests.POST.get('patient')).first():
#         return custom_response(False, message=" Bu ID da patient yo")
#
#     try:
#         file = Files(patient_id=requests.POST.get('patient'), file=requests.FILES.get('file'))
#         file.save()
#         return custom_response(True, data=file_format(file))
#     except:
#         return custom_response(False, message=MESSAGE['UndefinedError'])