from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import PasswordChangeForm


class MiFormularioDeRegistro(UserCreationForm):
    
    email = forms.CharField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {key: '' for key in fields}
        
class EditarPerfilFormulario(forms.Form):
    email = forms.CharField()
    first_name = forms.CharField(label='Nombre',required=False)
    last_name = forms.CharField(label='Apellido',required=False)
    avatar = forms.ImageField(label='Avatar',required=False)
    nacionalidad = forms.CharField(label='Nacionalidad',required=False)

class CambioDePassword(PasswordChangeForm):
    old_password = forms.CharField(label='Contraseña Antigua', widget=forms.PasswordInput)
    new_password1 = forms.CharField(label='Contraseña Nueva', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Repetir Contraseña Nueva', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
        help_texts = {key: '' for key in fields}