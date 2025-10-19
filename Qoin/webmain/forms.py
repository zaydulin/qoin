from django.utils.translation import gettext_lazy as _
from django import forms
from .models import Appeal



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