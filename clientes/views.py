from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Cliente
from .forms import ClienteCreateForm
from clientes.models import Cliente
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy

#Listar clientes
class ClienteListView(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'clientes/cliente_list.html'
    context_object_name = 'clientes'
    paginate_by = 10
    login_url = reverse_lazy('accounts_app:login')

# Crear clientes
class ClienteCreateView(LoginRequiredMixin, CreateView):
    model = Cliente
    form_class = ClienteCreateForm
    template_name = 'clientes/cliente_create.html'
    success_url = reverse_lazy('clientes_app:cliente_list')
    login_url = reverse_lazy('accounts_app:login')
    
    def form_valid(self, form):
        messages.success(self.request, 'Cliente registrado exitosamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error al registrar al cliente. Por favor, revisa los datos ingresados.')
        return super().form_invalid(form)

# Actualizar clientes
class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente
    form_class = ClienteCreateForm
    template_name = 'clientes/cliente_update.html'
    success_url = reverse_lazy('clientes_app:cliente_list')
    login_url = reverse_lazy('accounts_app:login')

# Eliminar clientes
class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    success_url = reverse_lazy('clientes_app:cliente_list')
    login_url = reverse_lazy('accounts_app:login')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Cliente eliminado con éxito')
        return super().delete(request, *args, **kwargs)
    
