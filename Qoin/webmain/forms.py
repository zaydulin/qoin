from django.utils.translation import gettext_lazy as _
from django import forms
from .models import Appeal, HighRiskRequest, FeedbackRequest


class AppealForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AppealForm, self).__init__(*args, **kwargs)
        self.fields['last_name'].widget.attrs['placeholder'] = _('Имя')
        self.fields['first_name'].widget.attrs['placeholder'] = _('Фамилия')
        self.fields['email'].widget.attrs['placeholder'] = _('Электронная почта')
        self.fields['subject'].widget.attrs['placeholder'] = _('Телефон')
        self.fields['message'].widget.attrs['placeholder'] = _('Введите ваше сообщение')

    class Meta:
        model = Appeal
        fields = ['last_name', 'first_name', 'email', 'subject', 'message']
        widgets = {
            'last_name': forms.TextInput(),
            'first_name': forms.TextInput(),
            'email': forms.EmailInput(),
            'subject': forms.TextInput(),
            'message': forms.Textarea(),
        }


class HighRiskRequestForm(forms.ModelForm):
    class Meta:
        model = HighRiskRequest
        fields = ['name', 'contact']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your name',
                'class': 'risk-form__input input'
            }),
            'contact': forms.TextInput(attrs={
                'placeholder': 'Your contact',
                'class': 'risk-form__input input'
            }),
        }

class FeedbackRequestForm(forms.ModelForm):
    class Meta:
        model = FeedbackRequest
        fields = ['website', 'name', 'phone', 'email', 'message']
        widgets = {
            'website': forms.TextInput(attrs={
                'placeholder': 'Your website',
                'class': 'feedback-section__input input'
            }),
            'name': forms.TextInput(attrs={
                'placeholder': 'Your name*',
                'class': 'feedback-section__input input',
                'required': True
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Your phone*',
                'class': 'feedback-section__input input',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Your e-mail',
                'class': 'feedback-section__input input'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Your message',
                'class': 'feedback-section__input input',
                'rows': 4
            }),
        }
