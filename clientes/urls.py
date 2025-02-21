# clientes
from django.urls import path
from . import views

app_name = "clientes_app"

urlpatterns = [
    path('cliente/list/', views.ClienteListView.as_view(), name='cliente_list'),
]