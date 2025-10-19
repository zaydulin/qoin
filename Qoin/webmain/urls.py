from django.urls import path
from django.contrib.auth import views as auth_views
app_name = 'webmain'
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contacts/', views.ContactView.as_view(), name='contact'),
    path('exchange/', views.ExchangeView.as_view(), name='exchange'),
    path('aml/', views.AMLKYCView.as_view(), name='aml'),
    path("page/<slug:slug>/", views.PageDetailView.as_view(), name="page"),

]