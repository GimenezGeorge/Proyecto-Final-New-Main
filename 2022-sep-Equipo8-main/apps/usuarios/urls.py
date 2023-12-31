from django.urls import path 
from . import views

app_name = "usuarios"

urlpatterns = [
	path("registrarme/", views.Registrarme.as_view(), name="registrarme"),
	path('detalle/<int:pk>/', views.Detalle.as_view(), name="detalle"),

    path('admin/listar/', views.ListarAdmin.as_view(), name="admin_listar"),
    path('admin/nuevo/', views.NuevoAdmin.as_view(), name="admin_nuevo"),
    path('admin/editar/<int:pk>/', views.EditarAdmin.as_view(), name="admin_editar"),
    path('admin/eliminar/<int:pk>/', views.EliminarAdmin.as_view(), name="admin_eliminar"),
    path("misusuarios/", views.MisUsuarios.as_view(), name="mis_usuarios"),
]