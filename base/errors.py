


INFORMATION = {
"NotData": {
        'uz': "Ma'lumot topilmadi",
        'en': "Patient not found",
        "ru": "Информация не найдена"
    },

"ErrorBig": {
        'uz': "Noma'lum xatolik",
        'en': "Unknown error",
        "ru": "Неизвестная ошибка"
    },


"NotDataTrID": {
        "uz": "Ushbu tr_id bo'yicha ma'lumot topilmadi",
        "ru": "Информация для этого tr_id не найдена",
        "en": "No information found for this tr_id"
    },

"MethodMust": {
        "uz": "Method bo'lishi shart",
        "ru": "Должен быть метод",
        "en": "Method must be filled"
    },
'ParamsNotFull': {
        "uz": "< params > to'lliq emas",
        "ru": "< params> неполные",
        "en": "< params > is incomplete"
    },

"NewNotFound": {
        "uz": "Bunday yangilik topilmadi",
        "ru": "Таких новостей не найдено",
        "en": "No such news was found",
    },


"DoctorNotFound": {
        "uz": "Bunday Id da doctor malumotlari topilmadi",
        "ru": "Таких DOCTOR не найдено",
        "en": "No such docotr was found",
    },
"Contactsadderror": {
        "uz": "Sizda contactlar mavjud",
        "ru": "davno yest",
        "en": "one",
    },

"Contactsdelet": {
        "uz": "contact o'chirildi",
        "ru": "delete",
        "en": "delete",
    },

"Doctordelet": {
        "uz": "doctor o'chirildi",
        "ru": "delete",
        "en": "delete",
    },
"Retsepdelet": {
        "uz": "retsep o'chirildi",
        "ru": "delete",
        "en": "delete",
    },

"Contactsdeleteerror": {
        "uz": "Sizda contact mavjud emas",
        "ru": "davno net",
        "en": "no contact",
    },

"Doctoradderror": {
        "uz": "Sizda doctor mavjud emas",
        "ru": "davno net",
        "en": "no contact",
    },

"Doctordeleteerror": {
        "uz": "Sizda doctor mavjud emas",
        "ru": "davno net",
        "en": "no contact",
    },
"Rertsepdeleteerror": {
        "uz": "Sizda retsep mavjud emas",
        "ru": "davno net",
        "en": "no retsep",
    },

"NewPutError": {
        "uz": "Id yuborib ko'ring",
        "ru": "davno net",
        "en": "no New",
    },

"NewGetError": {
        "uz": "Yangilik topilmadi",
        "ru": "davno net",
        "en": "no New",
    },

"NewGetIdError": {
        "uz": "Bu id da malumot yo'q topilmadi",
        "ru": "davno net",
        "en": "no New",
    },


"PatientNotFound": {
    "uz": "Bunday Id da kasal malumotlari topilmadi",
    "ru": "Таких karoche не найдено",
    "en": "No such kasalda karoche was found",
    },
"NewDelete": {
        'uz': "Yangilik  o'chirildi",
        'en': "The news has been deleted",
        "ru": "Новость удалена"
    },
    "NewDeleteError": {
        'uz': "Yangilik  o'chirishda muammo mavjud",
        'en': "There is a problem deleting news",
        "ru": "Не удалось удалить новость"
    },

"ErrorLang": {
        'uz': "Kerakli tilni yuboring",
        'en': "Submit the required language",
        "ru": "Введите требуемый язык"
    },
}



def error_unfilled(require):
    return {
        "uz": f"< {require} > bo'lishi shart",
        "ru": f"Должен быть < {require} >",
        "en": f"< {require} > must be filled"
    }