from collections import OrderedDict

from dashboard.models import Files, Diagnoz


def contact_format(data, lan):
    return OrderedDict([
        ("Id", data.id),

        ("phone_mobile", data.phone_mobile),
        ("phone_clinica", data.phone_clinica),
        ("email", data.email),
        ("adress", eval(f"data.adress_{lan}")),
        ("instagramm", data.instagramm),
        ("telegram", data.telegram),
        ("facebook", data.facebook),
        ("twitter", data.twitter),
        ("odnoklassniki", data.odnoklassniki),
        ("youtube", data.youtube),
        ("locatsiya", data.locatsiya),
    ])


def doctor_format_all(data, lan="uz"):
    return OrderedDict([

        ("Id", data.id),
        ("name", eval(f"data.name_{lan}")),
        ("first_name", eval(f"data.first_name_{lan}")),
        ("middle_name", eval(f"data.middle_name_{lan}")),
        ("specialty", eval(f"data.specialty_{lan}")),
        ("about_doctor", eval(f"data.about_doctor_{lan}")),
        ("phone", data.phone),
        ("email", data.email),
        ("instagramm", data.instagramm),
        ("telegram", data.telegram),
        ("facebook", data.facebook),
        ("twitter", data.twitter),
        ("odnoklassniki", data.odnoklassniki),
        ("image", "" if not data.image else data.image.url),

    ])


def patient_format_all(data):
    return OrderedDict([
        ("Id", data.id),
        ("name", data.name),
        ("first_name", data.first_name),
        ("father_name", data.father_name),
        ("age", data.age),
        ("phone", data.phone),

    ])


def file_format(data):
    return OrderedDict([
        ("Id", data.id),
        ("url", data.file.url),
        ("patient_id", data.patient_id),
    ])

 # files = [x.file.url for x in Files.objects.filter(patient_id=data.id)]
def patient_format_one(data):
    try:
        diagnoz = [diagnoz_format_all(x) for x in Diagnoz.objects.filter(patient_id=data.id)]
    except:
        diagnoz = None
    try:
        files = [{"file_id": x.id, "file_url": x.file.url} for x in Files.objects.filter(patient_id=data.id)]
    except:
        files = None

    return OrderedDict([
        ("Id", data.id),
        ("name", data.name),
        ("first_name", data.first_name),
        ("father_name", data.father_name),
        ("age", data.age),
        ("phone", data.phone),
        ("comment", data.comment),
        ("files", files),
        ("diagnoz", diagnoz),

    ])


def diagnoz_format_one(data):
    return OrderedDict([
        # ("patient", patient_format_one(data.patient)),
        ("patient", data.patient.id),
        ("Id_diagnoz", data.id),
        ("diagnoz", data.diagnoz),
        ("recommendation", data.recommendation),
        ("comment", data.comment),
        ("date", data.date),
        ("img_one", "" if not data.image_one else data.image_one.url),
        ("img_two", "" if not data.image_two else data.image_two.url)

    ])


def diagnoz_format_all(data):
    return OrderedDict([
        ("Id", data.id),
        ("diagnoz", data.diagnoz),
        ("date", data.date),
        ("patient", data.patient_id),
        ("patient_name", data.patient.name),
        ("patient_fist_name", data.patient.first_name),
        ("patient_father_name", data.patient.father_name),

    ])


def retsep_format_one(data, lan='uz'):
    return OrderedDict([
        ("Id", data.id),
        ("name_uz", data.name_uz),
        ("name_ru", data.name_ru),
        ("info_uz", data.info_uz),
        ("info_ru", data.info_ru),
    ])


def retsep_format_all(data, lan='ru'):
    return OrderedDict([
        ("Id", data.id),
        ("name", eval(f"data.name_{lan}")),
        ("info", eval(f"data.info_{lan}")),
    ])


def new_format_one(data, lan='uz'):
    return OrderedDict([
        ("Id", data.id),
        ("title", eval(f"data.title_{lan}")),
        ("short_desc", eval(f"data.short_desc_{lan}")),
        ("desc", eval(f"data.desc_{lan}")),
        ("date", data.date),
        ("image", "" if not data.image else data.image.url),
    ])


def new_format_all(data, lan='uz'):
    return OrderedDict([
        ("Id", data.id),
        ("image", "" if not data.image else data.image.url),
        ("title", eval(f"data.title_{lan}")),
        ("short_desc", eval(f"data.short_desc_{lan}")),
        ("date", data.date)

    ])


def contact_format_all(data):
    return OrderedDict([
        ("Id", data.id),
        ("phone_mobile", data.phone_mobile),
        ("phone_clinica", data.phone_clinica),
        ("email", data.email),
        ("adress_uz", data.adress_uz),
        ("adress_ru", data.adress_ru),
        ("adress_en", data.adress_en),
        ("instagramm", data.instagramm),
        ("telegram", data.telegram),
        ("facebook", data.facebook),
        ("twitter", data.twitter),
        ("odnoklassniki", data.odnoklassniki),
        ("youtube", data.youtube),
        ("locatsiya", data.locatsiya),

    ])
