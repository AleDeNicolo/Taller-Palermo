from django.urls import path
from AppCoder.views import mecanicos, inicio, service, cliente, entregables, serviceFormulario, mecanicosFormulario,busquedaChasis, buscar, login_request, register_request, editarPerfil, ClientesList, ClienteDetalle, ClienteCreacion, ClienteEdicion, ClienteEliminacion, About
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path("mecanicos/", mecanicos, name= "Mecanicos"),
    path("service/", service, name= "Service"),
    path("cliente/", cliente, name= "Cliente"),
    path("entregables/", entregables, name= "Entregables"),
    path("serviceFormulario/", serviceFormulario, name= "ServiceFormulario"),
    path("mecanicosFormulario/", mecanicosFormulario, name= "MecanicosFormulario"),
    path("busquedaChasis/", busquedaChasis, name= "BusquedaChasis"),
    path("buscar/", buscar, name= "Buscar"),
    path("", inicio, name= "Inicio"),
    path("about/", About, name= "About"),

    path('login', login_request, name='login'),
    path('register', register_request, name='registro'),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name='logout'),
    
    path('editarPerfil', editarPerfil, name='editarPerfil'),

    path('cliente/list/', ClientesList.as_view(), name='cliente_list'),
    path('cliente/<pk>', ClienteDetalle.as_view(), name='cliente_detalle'),
    path('cliente/nuevo/', ClienteCreacion.as_view(), name='cliente_crear'),
    path('cliente/editar/<pk>', ClienteEdicion.as_view(), name='cliente_editar'),
    path('cliente/borrar/<pk>', ClienteEliminacion.as_view(), name='cliente_borrar'),



]         

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = "AppCoder.views.page_not_found_view"