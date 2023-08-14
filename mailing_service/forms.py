from django import forms

from mailing_service.models import MessageSender


class StyleMixinForm:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name not in ['active', 'is_published']:
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-check-input'


class MessageSenderForm(StyleMixinForm, forms.ModelForm):

    class Meta:
        model = MessageSender
        fields = ['subject', 'body', 'start_date', 'end_date', 'frequency']

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')

        for f_word in FORBIDDEN_WORDS:
            if f_word in cleaned_data:
                raise forms.ValidationError('Поле название содержит запрещенные слова.')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')

        for f_word in FORBIDDEN_WORDS:
            if f_word in cleaned_data:
                raise forms.ValidationError('Поле описание содержит запрещенные слова.')

        return cleaned_data