from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(label="Correo electrónico")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")

class RegisterForm(forms.Form):
    email = forms.EmailField(label="Correo electrónico")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    role_choices = [
        ('user', 'Usuario'),
        ('admin', 'Administrador'),
    ]
    role = forms.ChoiceField(
        label="Rol",
        choices=role_choices,
        widget=forms.Select,  # Widget para un menú desplegable
    )

