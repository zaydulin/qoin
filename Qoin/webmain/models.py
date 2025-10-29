from django.db import models
from django.core.validators import (FileExtensionValidator)
from ckeditor.fields import RichTextField

class SettingsGlobale(models.Model):
    """Настройки сайта"""
    logo = models.FileField("Логотип",  upload_to='settings/%Y/%m/%d/', blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=['png', 'webp', 'jpeg', 'jpg', 'svg'])],)
    doplogo = models.FileField("Дополнительный логотип",  upload_to='settings/%Y/%m/%d/', blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=['png', 'webp', 'jpeg', 'jpg', 'svg'])],)
    favicon = models.FileField("Фавикон", upload_to='settings/%Y/%m/%d/', blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=['png', 'webp', 'jpeg', 'jpg', 'svg'])],)
    name = models.TextField("Название", blank=True, null=True)
    content = models.TextField("Копирайт",blank=True, null=True)
    description = models.TextField("Описание", blank=True, null=True)
    message_header = models.TextField("Шапка сообщения письма", blank=True, null=True)
    message_footer = models.TextField("Подвал сообщения письма", blank=True, null=True)
    yandex_metrica = models.TextField("Яндекс метрика", blank=True, null=True)
    google_analitic = models.TextField("Гугл аналитика", blank=True, null=True)

    class Meta:
        verbose_name = "Настройка сайта"
        verbose_name_plural = "Настройка сайта"

class HomePage(models.Model):
    """Главная страница"""
    preview = models.FileField(upload_to='settings/%Y/%m/%d/', blank=True, null=True, verbose_name="Превью", default='default/imagegallery/imagegellery_images.png', validators=[FileExtensionValidator(allowed_extensions=['png', 'webp', 'jpeg', 'jpg', 'svg'])],)
    title = models.CharField(verbose_name="Мета-заголовок", max_length=150, blank=True, null=True,)
    description = models.CharField(verbose_name="Мета-описание", max_length=255, blank=True, null=True,)
    propertytitle = models.CharField(verbose_name="Мета-заголовок ссылки", max_length=150, blank=True, null=True,)
    propertydescription = models.CharField(verbose_name="Мета-описание ссылки", max_length=255, blank=True, null=True,)
    slide_image1 = models.FileField(upload_to='settings/%Y/%m/%d/', blank=True, null=True, verbose_name="Первое изображение в слайде", default='default/imagegallery/imagegellery_images.png', validators=[FileExtensionValidator(allowed_extensions=['png', 'webp', 'jpeg', 'jpg', 'svg'])],)
    slide_image1_title = models.CharField(verbose_name="Заголовок первого изображения в слайде", max_length=150, blank=True, null=True,)
    slide_image1_description = models.CharField(verbose_name="Описание первого изображения в слайде", max_length=550, blank=True, null=True,)
    slide_button_link1 = models.CharField(verbose_name="Первая ссылка кнопки в слайде", max_length=550, blank=True, null=True,)
    slide_button_name1 = models.CharField(verbose_name="Первый заголовок кнопки в слайде", max_length=550, blank=True, null=True,)
    slide_image2 = models.FileField(upload_to='settings/%Y/%m/%d/', blank=True, null=True, verbose_name="Второго изображение в слайде", default='default/imagegallery/imagegellery_images.png', validators=[FileExtensionValidator(allowed_extensions=['png', 'webp', 'jpeg', 'jpg', 'svg'])],)
    slide_image2_title = models.CharField(verbose_name="Заголовок второе изображения в слайде", max_length=150, blank=True, null=True,)
    slide_image2_description = models.CharField(verbose_name="Описание второе изображения в слайде", max_length=550, blank=True, null=True,)
    slide_button_link2 = models.CharField(verbose_name="Вторая ссылка кнопки в слайде", max_length=550, blank=True, null=True,)
    slide_button_name2 = models.CharField(verbose_name="Второй заголовок кнопки в слайде", max_length=550, blank=True, null=True,)
    slide_image3 = models.FileField(upload_to='settings/%Y/%m/%d/', blank=True, null=True, verbose_name="Третье изображение в слайде", default='default/imagegallery/imagegellery_images.png', validators=[FileExtensionValidator(allowed_extensions=['png', 'webp', 'jpeg', 'jpg', 'svg'])],)
    slide_image3_title = models.CharField(verbose_name="Заголовок третьем изображения в слайде", max_length=150, blank=True, null=True,)
    slide_image3_description = models.CharField(verbose_name="Описание третьем изображения в слайде", max_length=550, blank=True, null=True,)
    slide_button_link3 = models.CharField(verbose_name="Третья ссылка кнопки в слайде", max_length=550, blank=True, null=True,)
    slide_button_name3 = models.CharField(verbose_name="Третий заголовок кнопки в слайде", max_length=550, blank=True, null=True,)
    block_2_image = models.FileField(upload_to='settings/%Y/%m/%d/', blank=True, null=True, verbose_name="Изображение во втором блоке", default='default/imagegallery/imagegellery_images.png', validators=[FileExtensionValidator(allowed_extensions=['png', 'webp', 'jpeg', 'jpg', 'svg'])],)
    block_2_h1 = models.CharField(verbose_name="Заголовок во втором блоке", max_length=150, blank=True, null=True,)
    block_2_title = models.CharField(verbose_name="Заголовок во втором блоке", max_length=150, blank=True, null=True,)
    block_2_description = models.CharField(verbose_name="Описание во втором блоке", max_length=550, blank=True, null=True,)
    block_2_button_link = models.CharField(verbose_name="Ссылка в кнопке во втором блоке", max_length=550, blank=True, null=True,)
    block_2_button_name = models.CharField(verbose_name="Заголовок в кнопке во втором блоке", max_length=550, blank=True, null=True,)
    block_3_image1 = models.FileField(upload_to='settings/%Y/%m/%d/', blank=True, null=True, verbose_name="Первое изображение в третьем блоке", default='default/imagegallery/imagegellery_images.png', validators=[FileExtensionValidator(allowed_extensions=['png', 'webp', 'jpeg', 'jpg', 'svg'])],)
    block_3_image1_title = models.CharField(verbose_name="Заголовок первого изображения в третьем блоке", max_length=150, blank=True, null=True,)
    block_3_image2 = models.FileField(upload_to='settings/%Y/%m/%d/', blank=True, null=True, verbose_name="Второго изображение в третьем блоке", default='default/imagegallery/imagegellery_images.png', validators=[FileExtensionValidator(allowed_extensions=['png', 'webp', 'jpeg', 'jpg', 'svg'])],)
    block_3_image2_title = models.CharField(verbose_name="Заголовок второе изображения в третьем блоке", max_length=150, blank=True, null=True,)
    block_3_image3 = models.FileField(upload_to='settings/%Y/%m/%d/', blank=True, null=True, verbose_name="Третье изображение в третьем блоке", default='default/imagegallery/imagegellery_images.png', validators=[FileExtensionValidator(allowed_extensions=['png', 'webp', 'jpeg', 'jpg', 'svg'])],)
    block_3_image3_title = models.CharField(verbose_name="Заголовок третьем изображения в третьем блоке", max_length=150, blank=True, null=True,)
    block_3_image4 = models.FileField(upload_to='settings/%Y/%m/%d/', blank=True, null=True, verbose_name="Четвертое изображение в третьем блоке", default='default/imagegallery/imagegellery_images.png', validators=[FileExtensionValidator(allowed_extensions=['png', 'webp', 'jpeg', 'jpg', 'svg'])],)
    block_3_image4_title = models.CharField(verbose_name="Заголовок четвертом изображения в третьем блоке", max_length=150, blank=True, null=True,)
    contact_top_h1 = models.CharField(verbose_name="Верхний заголовок H1 в контактах", max_length=150, blank=True, null=True,)
    contact_top_title = models.CharField(verbose_name="Верхнее описание в контактах", max_length=150, blank=True, null=True,)
    contact_top_description = models.CharField(verbose_name="Верхний заголовок в контактах", max_length=150, blank=True, null=True,)
    contact_description = models.CharField(verbose_name="Первое описание в контактах", max_length=150, blank=True, null=True,)
    contact_info_1 = models.CharField(verbose_name="Первое значение в контактах", max_length=150, blank=True, null=True,)
    contact_title_1 = models.CharField(verbose_name="Второе описание в контактах", max_length=150, blank=True, null=True,)
    contact_info_2 = models.CharField(verbose_name="Второе значение в контактах", max_length=150, blank=True, null=True,)
    contact_title_2 = models.CharField(verbose_name="Второе описание в контактах", max_length=150, blank=True, null=True,)
    block_4_h1 = models.CharField(verbose_name="Заголовок в четвертом блоке", max_length=150, blank=True, null=True,)
    block_4_title = models.CharField(verbose_name="Заголовок в четвертом блоке", max_length=150, blank=True, null=True,)
    block_4_description = models.CharField(verbose_name="Описание в четвертом блоке", max_length=550, blank=True, null=True,)
    block_4_image1 = models.FileField(upload_to='settings/%Y/%m/%d/', blank=True, null=True, verbose_name="Первое изображение в четвертом блоке", default='default/imagegallery/imagegellery_images.png', validators=[FileExtensionValidator(allowed_extensions=['png', 'webp', 'jpeg', 'jpg', 'svg'])],)
    block_4_image1_title = models.CharField(verbose_name="Заголовок первого изображения в четвертом блоке", max_length=150, blank=True, null=True,)
    block_4_image1_description = models.CharField(verbose_name="Описание первого изображения в четвертом блоке", max_length=550, blank=True, null=True,)
    block_4_image2 = models.FileField(upload_to='settings/%Y/%m/%d/', blank=True, null=True, verbose_name="Второго изображение в четвертом блоке", default='default/imagegallery/imagegellery_images.png', validators=[FileExtensionValidator(allowed_extensions=['png', 'webp', 'jpeg', 'jpg', 'svg'])],)
    block_4_image2_title = models.CharField(verbose_name="Заголовок второе изображения в четвертом блоке", max_length=150, blank=True, null=True,)
    block_4_image2_description = models.CharField(verbose_name="Описание второе изображения в четвертом блоке", max_length=550, blank=True, null=True,)
    block_4_image3 = models.FileField(upload_to='settings/%Y/%m/%d/', blank=True, null=True, verbose_name="Третье изображение в четвертом блоке", default='default/imagegallery/imagegellery_images.png', validators=[FileExtensionValidator(allowed_extensions=['png', 'webp', 'jpeg', 'jpg', 'svg'])],)
    block_4_image3_title = models.CharField(verbose_name="Заголовок третьем изображения в четвертом блоке", max_length=150, blank=True, null=True,)
    block_4_image3_description = models.CharField(verbose_name="Описание третьем изображения в четвертом блоке", max_length=550, blank=True, null=True,)
    block_4_image4 = models.FileField(upload_to='settings/%Y/%m/%d/', blank=True, null=True, verbose_name="Четвертое изображение в четвертом блоке", default='default/imagegallery/imagegellery_images.png', validators=[FileExtensionValidator(allowed_extensions=['png', 'webp', 'jpeg', 'jpg', 'svg'])],)
    block_4_image4_title = models.CharField(verbose_name="Заголовок четвертом изображения в четвертом блоке", max_length=150, blank=True, null=True,)
    block_4_image4_description = models.CharField(verbose_name="Описание четвертом изображения в четвертом блоке", max_length=550, blank=True, null=True,)
    block_5_profile1 = models.FileField(upload_to='settings/%Y/%m/%d/', blank=True, null=True, verbose_name="Первое изображение отзыва", default='default/imagegallery/imagegellery_images.png', validators=[FileExtensionValidator(allowed_extensions=['png', 'webp', 'jpeg', 'jpg', 'svg'])],)
    block_5_point1 = models.PositiveSmallIntegerField('Первая оценка', blank=False, default=1)
    block_5_profile1_description = models.CharField(verbose_name="Первый отзыв", max_length=550, blank=True, null=True,)
    block_5_profile1_name = models.CharField(verbose_name="Имя в первом отзыве", max_length=150, blank=True, null=True,)
    block_5_profile2 = models.FileField(upload_to='settings/%Y/%m/%d/', blank=True, null=True, verbose_name="Второе изображение отзыва", default='default/imagegallery/imagegellery_images.png', validators=[FileExtensionValidator(allowed_extensions=['png', 'webp', 'jpeg', 'jpg', 'svg'])],)
    block_5_point2 = models.PositiveSmallIntegerField('Вторая оценка', blank=False, default=1)
    block_5_profile2_description = models.CharField(verbose_name="Второй отзыв", max_length=550, blank=True, null=True,)
    block_5_profile2_name = models.CharField(verbose_name="Имя во втором отзыве", max_length=150, blank=True, null=True,)
    block_5_h1 = models.CharField(verbose_name="Заголовок в пятом  блоке", max_length=150, blank=True, null=True,)
    block_5_title = models.CharField(verbose_name="Заголовок в четвертом блоке", max_length=150, blank=True, null=True,)
    block_5_description = models.CharField(verbose_name="Описание в четвертом блоке", max_length=550, blank=True, null=True,)

    class Meta:
        verbose_name = "Главная страница"
        verbose_name_plural = "Главная страница"

class AboutPage(models.Model):
    """Cтраница о нас"""
    previev = models.FileField(upload_to='settings/%Y/%m/%d/', blank=True, null=True, verbose_name="Превью", default='default/imagegallery/imagegellery_images.png', validators=[FileExtensionValidator(allowed_extensions=['png', 'webp', 'jpeg', 'jpg', 'svg'])],)
    banner = models.FileField("Баннер", upload_to='settings/%Y/%m/%d/', blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=['png', 'webp', 'jpeg', 'jpg', 'svg'])],)

    title = models.CharField(verbose_name="Мета-заголовок", max_length=150, blank=True, null=True,)
    description = models.CharField(verbose_name="Мета-описание", max_length=255, blank=True, null=True,)
    propertytitle = models.CharField(verbose_name="Мета-заголовок ссылки", max_length=150, blank=True, null=True,)
    propertydescription = models.CharField(verbose_name="Мета-описание ссылки", max_length=255, blank=True, null=True,)
    block_1_image = models.FileField(upload_to='settings/%Y/%m/%d/', blank=True, null=True, verbose_name="Изображение в первом блоке", default='default/imagegallery/imagegellery_images.png', validators=[FileExtensionValidator(allowed_extensions=['png', 'webp', 'jpeg', 'jpg', 'svg'])],)
    block_1_title = models.CharField(verbose_name="Заголовок в первом блоке", max_length=150, blank=True, null=True,)
    block_1_description = models.TextField(verbose_name="Описание в первом блоке", blank=True, null=True,)
    block_2_image = models.FileField(upload_to='settings/%Y/%m/%d/', blank=True, null=True, verbose_name="Изображение во втором блоке", default='default/imagegallery/imagegellery_images.png', validators=[FileExtensionValidator(allowed_extensions=['png', 'webp', 'jpeg', 'jpg', 'svg'])],)
    block_2_h1 = models.CharField(verbose_name="Заголовок во втором блоке", max_length=150, blank=True, null=True,)
    block_2_title = models.CharField(verbose_name="Заголовок во втором блоке", max_length=150, blank=True, null=True,)
    block_2_description = models.CharField(verbose_name="Описание во втором блоке", max_length=550, blank=True, null=True,)
    block_2_button_link = models.CharField(verbose_name="Ссылка в кнопке во втором блоке", max_length=550, blank=True, null=True,)
    block_2_button_name = models.CharField(verbose_name="Заголовок в кнопке во втором блоке", max_length=550, blank=True, null=True,)
    block_3_h1 = models.CharField(verbose_name="Заголовок в третьем блоке", max_length=150, blank=True, null=True,)
    block_3_title = models.CharField(verbose_name="Заголовок в третьем блоке", max_length=150, blank=True, null=True,)
    block_3_description = models.CharField(verbose_name="Описание в третьем блоке", max_length=550, blank=True, null=True,)
    block_3_image1 = models.FileField(upload_to='settings/%Y/%m/%d/', blank=True, null=True, verbose_name="Первое изображение в третьем блоке", default='default/imagegallery/imagegellery_images.png', validators=[FileExtensionValidator(allowed_extensions=['png', 'webp', 'jpeg', 'jpg', 'svg'])],)
    block_3_image1_title = models.CharField(verbose_name="Заголовок первого изображения в третьем блоке", max_length=150, blank=True, null=True,)
    block_3_image1_description = models.CharField(verbose_name="Описание первого изображения в третьем блоке", max_length=550, blank=True, null=True,)
    block_3_image2 = models.FileField(upload_to='settings/%Y/%m/%d/', blank=True, null=True, verbose_name="Второго изображение в третьем блоке", default='default/imagegallery/imagegellery_images.png', validators=[FileExtensionValidator(allowed_extensions=['png', 'webp', 'jpeg', 'jpg', 'svg'])],)
    block_3_image2_title = models.CharField(verbose_name="Заголовок второе изображения в третьем блоке", max_length=150, blank=True, null=True,)
    block_3_image2_description = models.CharField(verbose_name="Описание второе изображения в третьем блоке", max_length=550, blank=True, null=True,)
    block_3_image3 = models.FileField(upload_to='settings/%Y/%m/%d/', blank=True, null=True, verbose_name="Третье изображение в третьем блоке", default='default/imagegallery/imagegellery_images.png', validators=[FileExtensionValidator(allowed_extensions=['png', 'webp', 'jpeg', 'jpg', 'svg'])],)
    block_3_image3_title = models.CharField(verbose_name="Заголовок третьем изображения в третьем блоке", max_length=150, blank=True, null=True,)
    block_3_image3_description = models.CharField(verbose_name="Описание третьем изображения в третьем блоке", max_length=550, blank=True, null=True,)
    block_3_image4 = models.FileField(upload_to='settings/%Y/%m/%d/', blank=True, null=True, verbose_name="Четвертое изображение в третьем блоке", default='default/imagegallery/imagegellery_images.png', validators=[FileExtensionValidator(allowed_extensions=['png', 'webp', 'jpeg', 'jpg', 'svg'])],)
    block_3_image4_title = models.CharField(verbose_name="Заголовок четвертом изображения в третьем блоке", max_length=150, blank=True, null=True,)
    block_3_image4_description = models.CharField(verbose_name="Описание четвертом изображения в третьем блоке", max_length=550, blank=True, null=True,)

    class Meta:
        verbose_name = "Cтраница о нас"
        verbose_name_plural = "Cтраница о нас"

class ContactPage(models.Model):
    """Cтраница контакты"""
    previev = models.FileField(upload_to='settings/%Y/%m/%d/', blank=True, null=True, verbose_name="Превью",
                               default='default/imagegallery/imagegellery_images.png', validators=[
            FileExtensionValidator(allowed_extensions=['png', 'webp', 'jpeg', 'jpg', 'svg'])], )
    title = models.CharField(verbose_name="Мета-заголовок", max_length=150, blank=True, null=True, )
    description = models.CharField(verbose_name="Мета-описание", max_length=255, blank=True, null=True, )
    propertytitle = models.CharField(verbose_name="Мета-заголовок ссылки", max_length=150, blank=True, null=True, )
    propertydescription = models.CharField(verbose_name="Мета-описание ссылки", max_length=255, blank=True, null=True, )
    contact_descriproin = models.TextField("Описание в подвале", blank=True, null=True)
    image = models.FileField(upload_to='settings/%Y/%m/%d/', blank=True, null=True, verbose_name="Изображение",
                               default='default/imagegallery/imagegellery_images.png', validators=[
            FileExtensionValidator(allowed_extensions=['png', 'webp', 'jpeg', 'jpg', 'svg'])],)
    contact_title_form = models.TextField("Заголовок над формой в контактах", blank=True, null=True)
    contact_title = models.TextField("Заголовок в контактах", blank=True, null=True)
    contact_content = models.TextField("Описание в контактах", blank=True, null=True)
    title_phone = models.CharField("Заголовок телефона",  max_length=15, blank=True, null=True)
    phone = models.CharField("Телефон",  max_length=15, blank=True, null=True)
    title_email = models.CharField("Заголовок Эл. Почты",  max_length=500, blank=True, null=True)
    email = models.CharField("Эл. Почта",  max_length=500, blank=True, null=True)
    title_adress = models.TextField("Заголовок адреса", blank=True, null=True)
    adress = models.TextField("Адрес", blank=True, null=True)
    map = models.TextField("Карта", blank=True, null=True)
    skype = models.TextField("Скайп", blank=True, null=True)
    telegram = models.TextField("Телеграм", blank=True, null=True)

    class Meta:
        verbose_name = "Cтраница контакты"
        verbose_name_plural = "Cтраница контакты"

class ExchangePage(models.Model):
    """Главная страница"""
    previev = models.FileField(upload_to='settings/%Y/%m/%d/', blank=True, null=True, verbose_name="Превью", default='default/imagegallery/imagegellery_images.png', validators=[FileExtensionValidator(allowed_extensions=['png', 'webp', 'jpeg', 'jpg', 'svg'])],)
    title = models.CharField(verbose_name="Мета-заголовок", max_length=150, blank=True, null=True,)
    description = models.CharField(verbose_name="Мета-описание", max_length=255, blank=True, null=True,)
    propertytitle = models.CharField(verbose_name="Мета-заголовок ссылки", max_length=150, blank=True, null=True,)
    propertydescription = models.CharField(verbose_name="Мета-описание ссылки", max_length=255, blank=True, null=True,)

    class Meta:
        verbose_name = "Обмен"
        verbose_name_plural = "Обмен"


class AMLKYCPage(models.Model):
    """Главная страница"""
    previev = models.FileField(upload_to='settings/%Y/%m/%d/', blank=True, null=True, verbose_name="Превью", default='default/imagegallery/imagegellery_images.png', validators=[FileExtensionValidator(allowed_extensions=['png', 'webp', 'jpeg', 'jpg', 'svg'])],)
    title = models.CharField(verbose_name="Мета-заголовок", max_length=150, blank=True, null=True,)
    description = models.CharField(verbose_name="Мета-описание", max_length=255, blank=True, null=True,)
    propertytitle = models.CharField(verbose_name="Мета-заголовок ссылки", max_length=150, blank=True, null=True,)
    propertydescription = models.CharField(verbose_name="Мета-описание ссылки", max_length=255, blank=True, null=True,)

    class Meta:
        verbose_name = "AML/KYC"
        verbose_name_plural = "AML/KYC"


class Appeal(models.Model):
    """Cтраница контакты"""
    last_name = models.CharField(verbose_name="Имя", max_length=150, blank=True, null=True, )
    first_name = models.CharField(verbose_name="Фамилия", max_length=150, blank=True, null=True, )
    email = models.CharField(verbose_name="Эл.Почта", max_length=150, blank=True, null=True, )
    subject = models.CharField(verbose_name="Телефон", max_length=150, blank=True, null=True, )
    message = models.TextField("Тектс", blank=True, null=True)

    class Meta:
        verbose_name = "Обращение"
        verbose_name_plural = "Обращения"



class Pages(models.Model):
    """Страницы"""
    PAGETYPE = [
        (1, 'Protection'),
        (2, 'Fintech'),
        (3, 'Business and commerce'),
        (4, 'Privacy policy'),
        (5, 'Terms of use'),
        (6, 'Partners'),
        (7, 'Help'),
        (8, 'Cookies'),
        (9, 'User agreement'),
    ]
    pagetype = models.PositiveSmallIntegerField('Тип', choices=PAGETYPE, blank=False, default=1)
    name = models.CharField("Название", max_length=250)
    description = RichTextField("Описание",db_index=True)
    slug = models.SlugField(max_length=140, unique=True)
    previev = models.FileField(upload_to='pages/%Y/%m/%d/', blank=True, null=True, verbose_name="Превью", default='default/imagegallery/imagegellery_images.png', validators=[FileExtensionValidator(allowed_extensions=['png', 'webp', 'jpeg', 'jpg', 'svg'])],)
    title = models.CharField(verbose_name="Мета-заголовок", max_length=150, blank=True, null=True,)
    metadescription = models.CharField(verbose_name="Мета-описание", max_length=255, blank=True, null=True,)
    propertytitle = models.CharField(verbose_name="Мета-заголовок ссылки", max_length=150, blank=True, null=True,)
    propertydescription = models.CharField(verbose_name="Мета-описание ссылки", max_length=255, blank=True, null=True,)
    publishet = models.BooleanField("Опубликован", default=False)
    setting = models.ForeignKey(
        SettingsGlobale,
        on_delete=models.CASCADE,
        related_name='pages',
        verbose_name='Настройки',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name



    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"

