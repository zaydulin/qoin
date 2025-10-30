from django.views.generic import TemplateView, DetailView
from webmain.models import HomePage, AboutPage, ContactPage, Appeal, Pages, ExchangePage, AMLKYCPage
from webmain.forms import AppealForm
from django.shortcuts import redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from django.template.loader import render_to_string

from webmain.forms import HighRiskRequestForm, FeedbackRequestForm


class CustomHtmxMixin:
    def get_template_names(self):
        is_htmx = bool(self.request.META.get('HTTP_HX_REQUEST'))
        if is_htmx:
            return [self.template_name]
        else:
            return ['include_block.html']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_htmx'] = self.template_name

        # Получаем SEO данные из View и передаем их для блоков
        seo_context = self.get_seo_context()
        context.update(seo_context)

        return context

    def get_seo_context(self):
        """
        Переопределите этот метод в дочерних классах
        чтобы вернуть SEO данные для этой страницы
        """
        return {
            'block_title': 'Заголовок по умолчанию',
            'block_description': 'Описание по умолчанию',
            'block_propertytitle': 'Property Title по умолчанию',
            'block_propertydescription': 'Property Description по умолчанию',
            'block_propertyimage': '',
            'block_head': ''
        }

class HomeView(CustomHtmxMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Получаем объект HomePage ОДИН раз
        try:
            home_page = HomePage.objects.first()
            context['home_page'] = home_page

            # Используем один объект для всех данных
            if home_page:
                # SEO данные для базового шаблона
                context.update({
                    'block_title': home_page.title,
                    'block_description': home_page.description,
                    'block_propertytitle': home_page.propertytitle,
                    'block_propertydescription': home_page.propertydescription,
                    'block_propertyimage': home_page.preview.url if home_page.preview else '',
                })

                # Дополнительные данные для шаблона (если нужны)
                context['seo_preview'] = home_page.preview
                context['seo_title'] = home_page.title
                context['seo_description'] = home_page.description
                context['seo_propertytitle'] = home_page.propertytitle
                context['seo_propertydescription'] = home_page.propertydescription

        except HomePage.DoesNotExist:
            # Устанавливаем значения по умолчанию
            context['home_page'] = None
            context['seo_preview'] = None
            context['seo_title'] = None
            context['seo_description'] = None
            context['seo_propertytitle'] = None
            context['seo_propertydescription'] = None

        return context

    def get_seo_context(self):
        """
        Переопределяем метод для получения SEO данных из базы
        """
        try:
            home_page = HomePage.objects.first()
            if home_page:
                return {
                    'block_title': home_page.title,
                    'block_description': home_page.description,
                    'block_propertytitle': home_page.propertytitle,
                    'block_propertydescription': home_page.propertydescription,
                    'block_propertyimage': home_page.preview.url if home_page.preview else '',
                    'block_head': ''
                }
        except HomePage.DoesNotExist:
            pass

        # Возвращаем значения по умолчанию, если нет данных
        return super().get_seo_context()

class AboutView(CustomHtmxMixin, TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = AboutPage.objects.first()
        if page:
            context['page'] = page
            context['seo_previev'] = page.previev
            context['banner'] = page.banner
            context['seo_title'] = page.title
            context['seo_description'] = page.description
            context['seo_propertytitle'] = page.propertytitle
            context['seo_propertydescription'] = page.propertydescription
        else:
            context['page'] = None
            context['seo_previev'] = None
            context['seo_title'] = None
            context['seo_description'] = None
            context['seo_propertytitle'] = None
            context['seo_propertydescription'] = None
        return context

class ContactView(CustomHtmxMixin, TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = ContactPage.objects.first()
        if page:
            context['page'] = page
            context['seo_previev'] = page.previev
            context['banner'] = page.image

            context['seo_title'] = page.title
            context['seo_description'] = page.description
            context['seo_propertytitle'] = page.propertytitle
            context['seo_propertydescription'] = page.propertydescription
        else:
            context['page'] = None
            context['seo_previev'] = None
            context['seo_title'] = None
            context['seo_description'] = None
            context['seo_propertytitle'] = None
            context['seo_propertydescription'] = None
        # Добавление формы в контекст
        context['form'] = AppealForm()
        return context

    def post(self, request, *args, **kwargs):
        form = AppealForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('webmain:contact')
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)

class ExchangeView(CustomHtmxMixin, TemplateView):
    template_name = 'cryptoexchange.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = ExchangePage.objects.first()
        if page:
            context['page'] = page
            context['seo_previev'] = page.previev

            context['seo_title'] = page.title
            context['seo_description'] = page.description
            context['seo_propertytitle'] = page.propertytitle
            context['seo_propertydescription'] = page.propertydescription
        else:
            context['page'] = None
            context['seo_previev'] = None
            context['seo_title'] = None
            context['seo_description'] = None
            context['seo_propertytitle'] = None
            context['seo_propertydescription'] = None
        # Добавление формы в контекст
        context['form'] = AppealForm()
        return context


class AMLKYCView(CustomHtmxMixin, TemplateView):
    template_name = 'aml.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = AMLKYCPage.objects.first()
        if page:
            context['page'] = page
            context['seo_previev'] = page.previev

            context['seo_title'] = page.title
            context['seo_description'] = page.description
            context['seo_propertytitle'] = page.propertytitle
            context['seo_propertydescription'] = page.propertydescription
        else:
            context['page'] = None
            context['seo_previev'] = None
            context['seo_title'] = None
            context['seo_description'] = None
            context['seo_propertytitle'] = None
            context['seo_propertydescription'] = None
        # Добавление формы в контекст
        context['form'] = AppealForm()
        return context


class PageDetailView(CustomHtmxMixin, DetailView):
    """Страница"""
    model = Pages
    template_name = 'page_detail.html'
    context_object_name = 'page'
    slug_field = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = context['page']
        if page:
            context['pageinformation'] = page.description
            context['seo_previev'] = page.previev
            context['seo_title'] = page.title
            context['seo_description'] = page.metadescription
            context['seo_propertytitle'] = page.propertytitle
            context['seo_propertydescription'] = page.propertydescription
        else:
            context['pageinformation'] = None
        return context


@require_http_methods(["POST"])
def high_risk_request(request):
    form = HighRiskRequestForm(request.POST)

    if form.is_valid():
        form.save()

        # Возвращаем сообщение об успехе
        success_html = """
        <div class="success-message">
            <h4 style="margin: 0 0 0.5rem 0; color: #155724;">✅ Thank you!</h4>
            <p style="margin: 0;">Our experts will contact you as soon as possible and advise on the terms of connection.</p>
        </div>
        """
        return HttpResponse(success_html)
    else:
        # Возвращаем сообщение об ошибке
        error_html = f"""
        <div class="error-message" style="background: #f8d7da; color: #721c24; padding: 1rem; border-radius: 5px; margin-top: 1rem; border: 1px solid #f5c6cb;">
            <p style="margin: 0 0 0.5rem 0;">Please correct the following errors:</p>
            <ul style="margin: 0; padding-left: 1rem;">
                {"".join(f'<li>{error}</li>' for field in form for error in field.errors)}
            </ul>
        </div>
        """
        return HttpResponse(error_html)


@require_http_methods(["POST"])
def feedback_request(request):
    form = FeedbackRequestForm(request.POST)

    if form.is_valid():
        form.save()

        # Успешный ответ
        success_html = """
        <div class="success-message" style="background: #d4edda; color: #155724; padding: 1.5rem; border-radius: 8px; margin-top: 1rem; border: 1px solid #c3e6cb; text-align: center;">
            <h4 style="margin: 0 0 1rem 0; color: #155724;">✅ Thank you!</h4>
            <p style="margin: 0;">Your message has been sent successfully. We will contact you soon.</p>
        </div>
        """
        return HttpResponse(success_html)
    else:
        # Форма с ошибками
        html = render_to_string('feedback_form_partial.html', {
            'form': form
        }, request=request)
        return HttpResponse(html)
