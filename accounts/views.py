from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from accounts.forms import MiFormularioDeRegistro, EditarPerfilFormulario, CambioDePassword
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import ExtensionUsuario

def mi_login(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            login(request, usuario)
            extensionUsuario, nuevo =ExtensionUsuario.objects.get_or_create(user=request.user)
            return redirect('index')
    else:
        formulario = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'formulario':formulario})

def registrar(request):
    
    if request.method == 'POST':
        formulario = MiFormularioDeRegistro(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('index')
    else:
        formulario = MiFormularioDeRegistro()
    
    return render(request, 'accounts/registrar.html', {'formulario':formulario})

@login_required
def perfil(request):
    return render(request, 'accounts/perfil.html', {})

@login_required
def editar_perfil(request):
    
    if request.method == 'POST':
        formulario = EditarPerfilFormulario(request.POST, request.FILES)
        
        if formulario.is_valid():
            data_nueva = formulario.cleaned_data
            request.user.first_name = data_nueva['first_name']
            request.user.last_name = data_nueva['last_name']
            request.user.email = data_nueva['email']
            request.user.extensionusuario.avatar = data_nueva['avatar']
            
            request.user.extensionusuario.save()
            request.user.save()
            return redirect('perfil')
    else:
        formulario = EditarPerfilFormulario(
            initial={
                'first_name': request.user.first_name,
                'last_name': request.user.last_name, 
                'email': request.user.email,
                'avatar': request.user.extensionusuario.avatar,
            }
        )
    return render(request, 'accounts/editar_perfil.html', {'formulario':formulario})
        
class CambiarContraseña(LoginRequiredMixin, PasswordChangeView):
    template_name = 'accounts/cambiar_contraseña.html'
    success_url = '/accounts/perfil/'
    form_class = CambioDePassword
      