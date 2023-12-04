from django.urls import path
from api_vehiculo import views

urlpatterns=[

    path('', views.Listar_vehiculo, name="Clientes"),
    path('detalle/<str:pk>', views.Detalle_vehiculo, name="Detalles_clientes"),
    path('crear', views.Registro_vehi, name="Registar_cleinte"),
    path('actualizar/<str:pk>/', views.Actualizar_vehiculo, name="Actualizar_cliente"),
    path('eliminar/<str:pk>/', views.Eliminar_vehiculo, name="Eliminar_cliente"),
]