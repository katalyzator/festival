# coding=utf-8
from django import forms


class RegistrationForm(forms.Form):
    film_name = forms.CharField(max_length=250, required=True)  # название фильма
    country = forms.CharField(max_length=250, required=True)  # какую страну представляет фильм
    director = forms.CharField(max_length=250, required=True)  # режиссер фильма
    language = forms.CharField(max_length=250, required=True)  # оригинальный язык фильма
    lang_tit = forms.CharField(max_length=250, required=True)  # язык титров
    chronological = forms.CharField(max_length=250, required=True)  # хронометраж фильма
    year = forms.CharField(max_length=250, required=True)  # год производства
    genre = forms.CharField(max_length=250, required=True)  # Жанр фильма
    filmtype = forms.CharField(max_length=250, required=True)  # Type of film
    url_film = forms.CharField(max_length=250, required=True)  # Ссылка на фильма

    company = forms.CharField(max_length=250, required=True)  # Компания производитель
    address = forms.CharField(max_length=250, required=False)  # Компания произвдитель
    phone_number = forms.CharField(max_length=250, required=False)  # номер телефона
    email = forms.EmailField(required=True)
    site = forms.CharField(max_length=250, required=True)  # Сайт если есть

    copyrighter = forms.CharField(max_length=250, required=True)  # pravoobladatel'
    contacts = forms.CharField(max_length=250, required=True)  # Контактные данные

    author = forms.CharField(max_length=250, required=True)  # Авторы сценария
    operator = forms.CharField(max_length=250, required=True)
    producer = forms.CharField(max_length=250, required=True)
    hudojnik = forms.CharField(max_length=250, required=True)
    actors = forms.CharField(max_length=1000, required=True)
    sinopsis = forms.CharField(max_length=250, required=True)

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['film_name'].label = "Название фильма(на русском)*"
        self.fields['country'].label = "Страна(какую страну представляет ваш фильм)*"
        self.fields['director'].label = "Режиссер (ФИО)*"
        self.fields['language'].label = "Оригинальный язык фильма*"
        self.fields['lang_tit'].label = "Язык титров*"
        self.fields['chronological'].label = "Хронометраж фильма*"
        self.fields['year'].label = "Год производства*"
        self.fields['genre'].label = "Жанр Фильма*"
        self.fields['filmtype'].label = "Формат*"
        self.fields['url_film'].label = "Ссылка на фильм с паролем (только VIMEO, DROPBOX, не больше 1,5 GB)*"
        self.fields[
            'company'].label = "Компания–производитель (Указывать полное название организации, студии или учебного заведения)*"
        self.fields['address'].label = "Адрес*"
        self.fields['phone_number'].label = "Номер Телефона"
        self.fields['email'].label = "E-mail*"
        self.fields['site'].label = "Сайт (если есть)"
        self.fields['copyrighter'].label = "Правообладатель*"
        self.fields['contacts'].label = "Контактные данные (адрес, тел., е-mail)*"
        self.fields['author'].label = "Автор сценария*"
        self.fields['operator'].label = "Оператор*"
        self.fields['producer'].label = "Продюсер*"
        self.fields['hudojnik'].label = "Художник*"
        self.fields['actors'].label = "Актеры*"
        self.fields['sinopsis'].label = "Синопсис*"


# class DirectorDetailForm(forms.Form):
#     name = forms.CharField(max_length=255, required=True)
#     date = forms.CharField(max_length=255, required=True)
#     education = forms.CharField(max_length=255, required=True)
#     biography = forms.CharField(max_length=255, required=True)
#     image = forms.FileField(upload_to='files/images', required=True)
#     fromfilm = forms.FileField(upload_to='files/images', required=True)
#
#     def __init__(self, *args, **kwargs):
#         super(DirectorDetailForm, self).__init__(*args, **kwargs)
#         self.fields['name'].label = "ФИО"
#         self.fields['date'].label = "Дата и место рождения"
