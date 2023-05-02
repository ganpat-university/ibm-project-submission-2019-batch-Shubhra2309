from django.contrib.auth.forms import AuthenticationForm


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Username'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Password'})
        self.fields['username'].label = ''
        self.fields['password'].label = ''
        self.fields['username'].help_text = ''
        self.fields['password'].help_text = ''
        self.error_messages['invalid_login'] = 'Invalid username or password.'
        self.template_name = 'login.html'
