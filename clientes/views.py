from django.shortcuts import render
from django.views.generic import ListView
from clientes.models import Cliente
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy



class ClienteListView(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'clientes/cliente_list.html'
    context_object_name = 'clientes'
    paginate_by = 10
    login_url = reverse_lazy('accounts_app:login')