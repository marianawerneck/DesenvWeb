from django.contrib.auth.forms import AuthenticationForm


class AuthenticationFormCustomizado(AuthenticationForm):

    error_messages = {
        'invalid_login': 'Login inválido',
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].error_messages={'required': 'Campo obrigatório'}
        self.fields['username'].widget.attrs.update({'class': 'form-control form-control-sm'})

        # <input type="text" name="username" autofocus="" autocapitalize="none" autocomplete="username"
        #        maxlength="150" required="" id="id_username">

        self.fields['password'].error_messages={'required': 'Campo obrigatório'}
        self.fields['password'].widget.attrs.update({'class': 'form-control form-control-sm'})

        # <input type="password" name="password" autocomplete="current-password" required=""
        #        id="id_password">
