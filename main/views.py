# coding=utf-8
import os

from django.core.mail import EmailMessage
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.template import Context
from django.template import Template
from django.views.decorators.csrf import csrf_exempt

from festival.settings import BASE_DIR
from .models import News, NewsImage

from main.form import RegistrationForm


# Create your views here.

def main(request):
    context = {}
    template = 'main/index.html'

    return render(request, template, context)


def all(request):
    news = News.objects.all()
    context = {"news": news}
    template = 'news.html'

    return render(request, template, context)


def single(request, id):
    try:
        news = News.objects.get(id=id)

        images = NewsImage.objects.filter(news=news)

        context = {"news": news, "images": images}
        template = 'single_post.html'

        return render(request, template, context)

    except News.DoesNotExist:
        raise Http404
    except NewsImage.DoesNotExist:
        raise Http404


def registration(request):
    context = {}
    template = 'form.html'

    return render(request, template, context)


@csrf_exempt
def send_mail(request):
    if request.method == 'POST':

        form = RegistrationForm(request.POST)

        if form.is_valid():
            film_name = form.cleaned_data['film_name']  # название фильма
            country = form.cleaned_data['country']  # какую страну представляет фильм
            director = form.cleaned_data['director']  # режиссер фильма
            language = form.cleaned_data['language']  # оригинальный язык фильма
            lang_tit = form.cleaned_data['lang_tit']  # язык титров
            chronological = form.cleaned_data['chronological']  # хронометраж фильма
            year = form.cleaned_data['year']  # год производства
            genre = form.cleaned_data['genre']  # Жанр фильма
            filmtype = form.cleaned_data['filmtype']  # Type of film
            url_film = form.cleaned_data['url_film']  # Ссылка на фильма

            company = form.cleaned_data['company']  # Компания производитель
            address = form.cleaned_data['address']  # Компания произвдитель
            phone_number = form.cleaned_data['phone_number']  # номер телефона
            email = form.cleaned_data['email']
            site = form.cleaned_data['site']  # Сайт если есть

            copyrighter = form.cleaned_data['copyrighter']  # pravoobladatel'
            contacts = form.cleaned_data['contacts']  # Контактные данные

            author = form.cleaned_data['author']  # Авторы сценария
            operator = form.cleaned_data['operator']
            producer = form.cleaned_data['producer']
            hudojnik = form.cleaned_data['hudojnik']
            actors = form.cleaned_data['actors']
            sinopsis = form.cleaned_data['sinopsis']

            f = open(os.path.join(BASE_DIR, "templates/mail.html"))

            content = f.read()
            f.close()

            context = Context(dict(film_name=film_name, country=country, director=director, language=language, \
                                   lang_tit=lang_tit, chronological=chronological, year=year, genre=genre, \
                                   filmtype=filmtype, url_film=url_film, company=company, address=address, \
                                   phone_number=phone_number, email=email, site=site, copyrighter=copyrighter, \
                                   contacts=contacts, author=author, operator=operator, producer=producer, \
                                   hudojnik=hudojnik, actors=actors, sinopsis=sinopsis
                                   ))
            template = Template(content)
            recipients = ['web.coder96@gmail.com']
            mail = EmailMessage('Заявка', template.render(context), to=recipients)
            mail.content_subtype = 'html'
            mail.send()
            return HttpResponse('.')
        else:
            return HttpResponse('error')

    else:
        form = RegistrationForm()


def registrationView(request):
    context = {"form": RegistrationForm}
    template = 'forms.html'
    return render(request, template, context)


def about_view(request):
    context = {}
    template = 'about.html'

    return render(request, template, context)

def reglament_view(request):
    context = {}
    template = 'reglament.html'

    return render(request, template, context)