from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Div
from crispy_forms.bootstrap import PrependedText, FormActions


class UsersLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(UsersLoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.layout = Layout(
            "username",
            "password",
            FormActions(Submit("submit", "Login", css_class="btn btn-block btn-lg")),
        )

    def clean(self, *args, **keyargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = None
            try:
                user = User.objects.get(username=username)
            except:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect Password")
            if not user.is_active:
                raise forms.ValidationError("User is no longer active")

        return super(UsersLoginForm, self).clean(*args, **keyargs)


class UsersRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "confirm_password",
        ]

    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(UsersRegisterForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {
                "class": "form-control",
                "name": "username",
                "placeholder": "abdurrahim101",
            }
        )
        self.fields["password"].widget.attrs.update(
            {"class": "form-control", "name": "password"}
        )
        self.fields["confirm_password"].widget.attrs.update(
            {"class": "form-control", "name": "confirm_password"}
        )
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.layout = Layout(
            "username",
            Row(
                Column("password", css_class="form-group col-md-6 mb-0"),
                Column("confirm_password", css_class="form-group col-md-6 mb-0"),
            ),
            FormActions(Submit("submit", "Register", css_class="btn btn-block btn-lg")),
        )

    def clean(self, *args, **keyargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                "Username already taken. Try something little different"
            )

        if password != confirm_password:
            raise forms.ValidationError("Passwords must match")

        if password and len(password) < 8:
            raise forms.ValidationError("Password must be greater than 8 characters")

        return super(UsersRegisterForm, self).clean(*args, **keyargs)
