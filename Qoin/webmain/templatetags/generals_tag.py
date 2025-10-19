from django import template
from webmain.models import SettingsGlobale, ContactPage, Pages

register = template.Library()

@register.simple_tag()
def get_current_name():
    return SettingsGlobale.objects.first().name

@register.simple_tag()
def get_current_content():
    return SettingsGlobale.objects.first().content

@register.simple_tag()
def get_current_description():
    return SettingsGlobale.objects.first().description

@register.simple_tag()
def get_current_yandex_metrica():
    return SettingsGlobale.objects.first().yandex_metrica

@register.simple_tag()
def get_current_google_analitic():
    return SettingsGlobale.objects.first().google_analitic

@register.simple_tag()
def get_current_favicon():
    return SettingsGlobale.objects.first().favicon.url


@register.simple_tag()
def get_current_logo():
    return SettingsGlobale.objects.first().logo.url

@register.simple_tag()
def get_current_doplogo():
    return SettingsGlobale.objects.first().doplogo.url

@register.simple_tag()
def get_current_contact_descriproin():
    return ContactPage.objects.first().contact_descriproin

@register.simple_tag()
def get_current_phone():
    return ContactPage.objects.first().phone

@register.simple_tag()
def get_current_email():
    return ContactPage.objects.first().email

@register.simple_tag()
def get_current_adress():
    return ContactPage.objects.first().adress

@register.simple_tag()
def get_current_skype():
    return ContactPage.objects.first().skype

@register.simple_tag()
def get_current_telegram():
    return ContactPage.objects.first().telegram

@register.simple_tag
def get_all_pages():
    return Pages.objects.filter(publishet=True)

