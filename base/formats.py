from collections import OrderedDict


from dashboard.models import Files


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


def doctor_format(data, lan="uz"):
    return OrderedDict([
        ("Id", data.id),
        ("name", eval(f"data.name_{lan}")),
        ("first_name", eval(f"data.first_name_{lan}")),
        ("middle_name", eval(f"data.middle_name_{lan}")),
        ("specialty", eval(f"data.specialty_{lan}")),
        ("about_doctor", eval(f"data.about_doctor_{lan}")),
        # ("motto", eval(f"data.motto_{lan}")),
        ("phone", data.phone),

        ("email", data.email),

        ("instagramm", data.instagramm),
        ("telegram", data.telegram),
        ("facebook", data.facebook),
        ("twitter", data.twitter),
        ("odnoklassniki", data.odnoklassniki),
        ("img", data.img.url),

    ])


def new_format(data, lan):
    return OrderedDict([
        ("Id", data.id),
        ("img", data.img.url),
        ("title", eval(f"data.title_{lan}")),
        ("short_desc", eval(f"data.short_desc_{lan}")),

    ])


def new_format_all(data, lan):
    return OrderedDict([
        ("Id", data.id),
        ("img", data.img.url),
        ("title", eval(f"data.title_{lan}")),
        ("short_desc", eval(f"data.short_desc_{lan}")),
        ("desc", eval(f"data.desc_{lan}")),
        ("date", data.date)

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


def patient_format_one(data):
    try:
        files = [x.file.url for x in Files.objects.filter(patient_id=data.id)]
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

    ])


def diagnoz_format_one(data):


    return OrderedDict([
        ("Id", data.id),
        ("diagnoz", data.diagnoz),
        ("recommendation", data.recommendation),
        ("comment", data.comment),
        ("date", data.date),
        ("img_one", data.image_one.url),
        ("img_two", data.image_two.url),
        ("patient", data.patient.name),

    ])


def diagnoz_format_all(data):
    return OrderedDict([
        ("Id", data.id),
        ("diagnoz", data.diagnoz),
        ("date", data.date),
        ("patient", data.patient_id),

    ])


def retsep_format_one(data):
    return OrderedDict([
        ("Id", data.id),
        ("name", data.name),
        ("info", data.info),
    ])


def retsep_format_all(data):
    return OrderedDict([
        ("Id", data.id),
        ("name", data.name),


    ])
