# clientes
from django.urls import path
from . import views

app_name = "clientes_app"

urlpatterns = [
    path('cliente/list/', views.ClienteListView.as_view(), name='cliente_list'),
    path('cliente/create/', views.ClienteCreateView.as_view(), name='cliente_create'),
    path('cliente/update/<int:pk>/', views.ClienteUpdateView.as_view(), name='cliente_update'),
    path('cliente/delete/<int:pk>/', views.ClienteDeleteView.as_view(), name='cliente_delete'),
]