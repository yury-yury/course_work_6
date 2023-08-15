from django import forms

from mailing_service.models import MessageSender, Customer


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


class CustomerForm(StyleMixinForm, forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['name', 'email', 'description']
