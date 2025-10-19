from django.views.generic import TemplateView, DetailView
from webmain.models import HomePage, AboutPage, ContactPage, Appeal, Pages, ExchangePage, AMLKYCPage
from webmain.forms import AppealForm
from django.shortcuts import redirect

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            home_page = HomePage.objects.first()
            context['home_page'] = home_page
        except HomePage.DoesNotExist:
            context['home_page'] = None
        try:
            seo_data = HomePage.objects.first()
            context['seo_previev'] = seo_data.previev
            context['seo_title'] = seo_data.title
            context['seo_description'] = seo_data.description
            context['seo_propertytitle'] = seo_data.propertytitle
            context['seo_propertydescription'] = seo_data.propertydescription
        except HomePage.DoesNotExist:
            context['seo_previev'] = None
            context['seo_title'] = None
            context['seo_description'] = None
            context['seo_propertytitle'] = None
            context['seo_propertydescription'] = None
        return context

class AboutView(TemplateView):
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

class ContactView(TemplateView):
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

class ExchangeView(TemplateView):
    template_name = 'cryptoexchange.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = ExchangePage.objects.first()
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


class AMLKYCView(TemplateView):
    template_name = 'aml.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = AMLKYCPage.objects.first()
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


class PageDetailView(DetailView):
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
