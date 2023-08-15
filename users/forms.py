from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm
from django import forms
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ValidationError
from django.utils.crypto import get_random_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from mailing_service.forms import StyleMixinForm
from users.models import User


class UserRegisterForm(StyleMixinForm, UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserProfileForm(StyleMixinForm, UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()


class UserPasswordResetForm(StyleMixinForm, PasswordResetForm):

    class Meta:
        model = User
        fields = ('email', )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email and User.objects.filter(email=email).exists():
            return email
        else:
            raise ValidationError("Зарегистрированного пользователя с данным Email не существует")

    def save(
        self,
        domain_override=None,
        subject_template_name="registration/password_reset_subject.txt",
        email_template_name="registration/password_reset_email.html",
        use_https=False,
        token_generator=default_token_generator,
        from_email=None,
        request=None,
        html_email_template_name=None,
        extra_email_context=None,
    ):
        """
        Generate a one-use only link for resetting password and send it to the
        user.
        """
        email = self.cleaned_data["email"]

        if not domain_override:
            current_site = get_current_site(request)
            site_name = current_site.name
            domain = current_site.domain
        else:
            site_name = domain = domain_override
        email_field_name = User.get_email_field_name()

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return "Зарегистрированного пользователя с данным email не существует"

        password = get_random_string(10)
        user.set_password(password)
        user.save()

        for user in self.get_users(email):
            user_email = getattr(user, email_field_name)
            context = {
                "email": user_email,
                "password": password,
                # "domain": domain,
                "site_name": site_name,
                # "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                # "user": user,
                # "token": token_generator.make_token(user),
                # "protocol": "https" if use_https else "http",
                **(extra_email_context or {}),
            }
            self.send_mail(
                "users/password_reset_subject.html",
                "users/password_reset_email.html",
                context,
                from_email,
                user_email,
                html_email_template_name=html_email_template_name,
            )
