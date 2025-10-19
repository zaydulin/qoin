from django.contrib import admin
from django.http import HttpResponseRedirect
from modeltranslation.admin import TranslationAdmin

from .models import *
from django.utils.safestring import mark_safe
from django.urls import reverse

# Register your models here.

@admin.register(SettingsGlobale)
class SettingsGlobaleAdmin(admin.ModelAdmin):
    readonly_fields = ('get_image_logo', 'get_image_doplogo', 'get_image_favicon',)

    def get_image_logo(self, obj):
        if obj.logo:
            return mark_safe(f'<img src="{obj.logo.url}" width="50">')
        return "Нет изображения"
    get_image_logo.short_description = "Логотип"

    def get_image_doplogo(self, obj):
        if obj.doplogo:
            return mark_safe(f'<img src="{obj.doplogo.url}" width="50">')
        return "Нет изображения"
    get_image_doplogo.short_description = "Светлый логотип"

    def get_image_favicon(self, obj):
        if obj.favicon:
            return mark_safe(f'<img src="{obj.favicon.url}" width="50">')
        return "Нет изображения"
    get_image_favicon.short_description = "Фавикон"

    def has_add_permission(self, request):
        # Allow add if there are no HomePage objects in the database
        if not SettingsGlobale.objects.exists():
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_urls(self):
        from django.urls import path
        urls = super().get_urls()
        my_urls = [
            path('', self.redirect_to_edit),
        ]
        return my_urls + urls

    def redirect_to_edit(self, request):
        try:
            obj = SettingsGlobale.objects.get()
            url = reverse('admin:webmain_settingsglobale_change', args=[obj.pk])
        except SettingsGlobale.DoesNotExist:
            url = reverse('admin:webmain_settingsglobale_add')
        return HttpResponseRedirect(url)

    fieldsets = (
        (None, {
            'fields': (
                'logo', 'get_image_logo',
                'doplogo', 'get_image_doplogo',
                'favicon', 'get_image_favicon',
                'name', 'content', 'description',
                'message_header', 'message_footer',
                'yandex_metrica', 'google_analitic',
            ),
        }),
    )
@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    readonly_fields = ('get_image_preview',)

    def get_image_preview(self, obj):
        if obj.previev:
            return mark_safe(f'<img src="{obj.previev.url}" width="50">')
        return "Нет изображения"
    get_image_preview.short_description = "Логотип"

    def has_add_permission(self, request):
        # Allow add if there are no HomePage objects in the database
        if not HomePage.objects.exists():
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_urls(self):
        from django.urls import path
        urls = super().get_urls()
        my_urls = [
            path('', self.redirect_to_edit),
        ]
        return my_urls + urls

    def redirect_to_edit(self, request):
        try:
            obj = HomePage.objects.get()
            url = reverse('admin:webmain_homepage_change', args=[obj.pk])
        except HomePage.DoesNotExist:
            url = reverse('admin:webmain_homepage_add')
        return HttpResponseRedirect(url)

    fieldsets = (
        (None, {
            'fields': ('previev', 'get_image_preview', 'title', 'description', 'propertytitle', 'propertydescription'),
        }),
        ('Слайд', {
            'fields': (
                'slide_image1', 'slide_image1_title', 'slide_image1_description', 'slide_button_link1', 'slide_button_name1',
                'slide_image2', 'slide_image2_title', 'slide_image2_description', 'slide_button_link2', 'slide_button_name2',
                'slide_image3', 'slide_image3_title', 'slide_image3_description', 'slide_button_link3', 'slide_button_name3',
            ),
        }),
        ('Второй блок', {
            'fields': ('block_2_image', 'block_2_h1', 'block_2_title', 'block_2_description', 'block_2_button_link', 'block_2_button_name'),
        }),
        ('Третий блок', {
            'fields': (
                'block_3_image1', 'block_3_image1_title',
                'block_3_image2', 'block_3_image2_title',
                'block_3_image3', 'block_3_image3_title',
                'block_3_image4', 'block_3_image4_title',
            ),
        }),
        ('Блок контактов', {
            'fields': (
                'contact_top_h1', 'contact_top_title', 'contact_top_description',
                'contact_description', 'contact_title_1', 'contact_info_1',
                'contact_title_2', 'contact_info_2',
            ),
        }),
        ('Четвертый блок', {
            'fields': (
                'block_4_h1', 'block_4_title', 'block_4_description',
                'block_4_image1', 'block_4_image1_title', 'block_4_image1_description',
                'block_4_image2', 'block_4_image2_title', 'block_4_image2_description',
                'block_4_image3', 'block_4_image3_title', 'block_4_image3_description',
                'block_4_image4', 'block_4_image4_title', 'block_4_image4_description',
            ),
        }),
        ('Пятый блок (Отзывы)', {
            'fields': (
                'block_5_h1', 'block_5_title', 'block_5_description',
                'block_5_profile1', 'block_5_point1', 'block_5_profile1_description', 'block_5_profile1_name',
                'block_5_profile2', 'block_5_point2', 'block_5_profile2_description', 'block_5_profile2_name',
            ),
        }),
    )

@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    readonly_fields = ('get_image_previev',)

    def get_image_previev(self, obj):
        return mark_safe(f'<img src="{obj.previev.url}" width="50">')
    get_image_previev.short_description = "Логотип"

    def has_add_permission(self, request):
        # Allow add if there are no HomePage objects in the database
        if not AboutPage.objects.exists():
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_urls(self):
        from django.urls import path
        urls = super().get_urls()
        my_urls = [
            path('', self.redirect_to_edit),
        ]
        return my_urls + urls

    def redirect_to_edit(self, request):
        try:
            obj = AboutPage.objects.get()
            url = reverse('admin:webmain_aboutpage_change', args=[obj.pk])
        except AboutPage.DoesNotExist:
            url = reverse('admin:webmain_aboutpage_add')
        return HttpResponseRedirect(url)

    fieldsets = (
        (None, {
            'fields': ('banner','previev', 'get_image_previev', 'title', 'title_en',  'description', 'description_en', 'propertytitle','propertytitle_en', 'propertydescription','propertydescription_en',),
        }),
        ('Первый блок', {
            'fields': ('block_1_image', 'block_1_title', 'block_1_title_en', 'block_1_description', 'block_1_description_en'),
        }),
        ('Второй блок', {
            'fields': ('block_2_image', 'block_2_h1', 'block_2_h1_en', 'block_2_title',  'block_2_title_en','block_2_description','block_2_description_en',
                       'block_2_button_link', 'block_2_button_link_en', 'block_2_button_name', 'block_2_button_name_en'),
        }),
        ('Третий блок', {
            'fields': ('block_3_h1', 'block_3_h1_en', 'block_3_title', 'block_3_title_en', 'block_3_description', 'block_3_description_en',
                       'block_3_image1', 'block_3_image1_title', 'block_3_image1_description',
                       'block_3_image1_title_en', 'block_3_image1_description_en',
                       'block_3_image2', 'block_3_image2_title', 'block_3_image2_description',
                       'block_3_image2_title_en', 'block_3_image2_description_en',
                       'block_3_image3', 'block_3_image3_title', 'block_3_image3_description',
                       'block_3_image3_title_en', 'block_3_image3_description_en',
                       'block_3_image4', 'block_3_image4_title', 'block_3_image4_description',
                       'block_3_image4_title_en', 'block_3_image4_description_en',
                       ),
        }),
    )



@admin.register(ContactPage)
class ContactPageAdmin(admin.ModelAdmin):
    readonly_fields = ('get_image_previev',)

    def get_image_previev(self, obj):
        return mark_safe(f'<img src="{obj.previev.url}" width="50">')
    get_image_previev.short_description = "Логотип"

    def has_add_permission(self, request):
        # Allow add if there are no HomePage objects in the database
        if not ContactPage.objects.exists():
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_urls(self):
        from django.urls import path
        urls = super().get_urls()
        my_urls = [
            path('', self.redirect_to_edit),
        ]
        return my_urls + urls

    def redirect_to_edit(self, request):
        try:
            obj = HomePage.objects.get()
            url = reverse('admin:webmain_contactpage_change', args=[obj.pk])
        except HomePage.DoesNotExist:
            url = reverse('admin:webmain_contactpage_add')
        return HttpResponseRedirect(url)

    fieldsets = (
        (None, {
            'fields': ('get_image_previev', 'previev', 'title_en', 'title', 'description_en', 'description', 'propertytitle_en', 'propertytitle',
                       'propertydescription_en','propertydescription', 'contact_descriproin_en',  'contact_descriproin', 'image',
                        'contact_title_form_en', 'contact_title_form','contact_title_en','contact_title','contact_content_en', 'contact_content',
                       'title_phone_en','title_phone', 'phone','title_email_en','title_email', 'email', 'adress_en','adress', 'map', 'skype', 'telegram'),
        }),
    )

@admin.register(Appeal)
class AppealAdmin(admin.ModelAdmin):
    list_display = ["last_name", "email", "subject",]



@admin.register(Pages)
class PagesAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description"]
    prepopulated_fields = {"slug": ('name',), }
    list_display_links = ["id", "name", "description"]
    save_as = True
    save_on_top = True

admin.site.register(AMLKYCPage)
admin.site.register(ExchangePage)