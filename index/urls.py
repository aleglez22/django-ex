from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy

from . import views

app_name ='index'

urlpatterns = [

    #url(r'^/(?P<var1>\d+)/$', 'renderizar', name='renderizar')
    url(r'^$', views.ListaOrdenes.as_view(), name= "home-page"),
    url(r'^agregarCliente/$', views.agregarClienteOrden, name= "Agregar-Cliente-Orden"),
    url(r'^redirect/$', views.redirect_by_id, name= "Redirect-To-Orden"),
    url(r'^orden/(?P<pk>[0-9]+)/$', views.DetalleOrdenes.as_view(), name='Detalle-Ordenes'),
    url(r'^orden/(?P<pk>[0-9]+)/imprimir/$', views.ImprimirOrden, name='Imprimir-Orden'),
    url(r'orden/add/$', views.CrearOrden.as_view(), name='Add-Orden'),
    url(r'orden/add/(?P<cliente>[0-9]+)$', views.CrearOrden2.as_view(), name='Add-Orden2'),

    url(r'^orden/update/(?P<pk>[0-9]+)/$', views.EditarOrden.as_view(), name='Editar-Ordenes'),
    url(r'^orden/(?P<pk>[0-9]+)/delete/$', views.EliminarOrden.as_view(), name='Eliminar-Ordenes'),
    url(r'^orden/lista/$', views.TodasOrdenes.as_view(), name='Lista-Ordenes'),
    url(r'^file/$', views.ExcelExport, name='Exportar-Excel'),

    


    #Cliente urls
    url(r'^cliente/$', views.ListaCliente.as_view(), name='Home-Cliente'),
    url(r'cliente/add/$', views.CrearCliente.as_view(), name='Add-Cliente'),
    #nunca poner en una url un pedazo de url que ya esté definido porque no utilizará el metodo
    #get_success_url y solo utilizara el get_absolute_url
    url(r'orden/cliente-add/$', views.CrearClienteFromOrden.as_view(), name='Add-Cliente-From-Orden'),
    url(r'orden/equipo-add/$', views.CrearEquipoFromOrden.as_view(), name='Add-Equipo-From-Orden'),
    url(r'^cliente/update/(?P<pk>[0-9]+)/$', views.EditarCliente.as_view(), name='Editar-Cliente'),
    url(r'^cliente/(?P<pk>[0-9]+)/delete/$', views.EliminarCliente.as_view(), name='Eliminar-Cliente'),
    url(r'^cliente/equipo/(?P<pk>[0-9]+)/$', views.DetalleCliente.as_view(), name='Equipos-Cliente'),

    #EQUIPO urls
    url(r'^equipo/$', views.ListaEquipo.as_view(), name='Home-Equipo'),
    url(r'equipo/add/$', views.CrearEquipo.as_view(), name='Add-Equipo'),
    url(r'^equipo/(?P<pk>[0-9]+)/delete/$', views.EliminarEquipo.as_view(), name='Eliminar-Equipo'),
    
    #TECNICO urls
    url(r'^tecnico/$', views.ListaTecnico.as_view(), name='Home-Tecnico'),
    url(r'tecnico/add/$', views.CrearTecnico.as_view(), name='Add-Tecnico'),
    url(r'^tecnico/(?P<pk>[0-9]+)/delete/$', views.EliminarTecnico.as_view(), name='Eliminar-Tecnico'),

]