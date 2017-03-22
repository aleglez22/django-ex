from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model

# Create your models here.

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='eliminado')[0]

class Cliente (models.Model):
    Nombre = models.CharField(max_length = 30, )
    Apellido= models.CharField(max_length = 30,null=True, blank=True)
    Cedula= models.IntegerField(null=False, blank=False, unique = True)
    Direccion= models.CharField(max_length = 250,null=True, blank=True)
    Email= models.CharField(max_length = 250,null=True, blank=True)
    Fecha_ingreso= models.DateField(auto_now=True)
    Gasto_acumulado    = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    Telefono1= models.IntegerField(null=True, blank=True)
    Telefono2= models.IntegerField(null=True, blank=True)
    
    def get_absolute_url(self):
        return reverse('index:Home-Cliente')

    def __str__(self):
        return str(self.Cedula)+ " "+self.Nombre+ " "+self.Apellido

    

class Equipo (models.Model):
#id se genera automatico tipo AutoField
    Marca = models.CharField(max_length = 30)
    Modelo= models.CharField(max_length = 30)
    Serial =models.CharField(max_length = 40, null=True, blank=True)
    Tipo =models.CharField(max_length = 20, null=True, blank=True)
    Color =models.CharField(max_length = 20, null=True, blank=True)
    Cliente= models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    Fecha_creacion = models.DateField(auto_now=True, auto_now_add=False)

    def get_absolute_url(self):
        return reverse('index:Home-Equipo')


    def __str__(self):
        return str(self.Tipo) + " "+ str(self.Marca)+ " "+str(self.Modelo)


class Tecnico (models.Model):
    Nombre = models.CharField(max_length = 30)
    Apellido= models.CharField(max_length = 30, null=True, blank=True)
    Fecha_ingreso= models.DateField(auto_now=True)

    def get_absolute_url(self):
        return reverse('index:Home-Tecnico')
    
    def __str__(self):
        return self.Nombre


class Orden (models.Model):
    Fecha_creacion = models.DateField(auto_now=True, auto_now_add=False)
    Fecha_entrega= models.DateField(null=True, blank=True)
    Estado_inicial = models.CharField(max_length = 250, null=True, blank=True)#como llego el equipo
    Falla = models.CharField(max_length = 250, null=True, blank=True)
    Costo_reparacion = models.DecimalField(max_digits=6,decimal_places=2, null=True, blank=True)
    Costo_revision = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    Notas = models.CharField(max_length = 250, null=True, blank=True)
    Fecha_ofrecida = models.DateField(null=True, blank=True)
    Accesorios = models.CharField(max_length = 250,null=True, blank=True)
    Limite_garantia=  models.CharField(max_length = 20,null=True, blank=True)
    Informe_tecnico = models.CharField(max_length = 250,null=True, blank=True)
    Tecnico= models.ForeignKey(Tecnico, on_delete=models.SET(get_sentinel_user))
    Equipo= models.ForeignKey(Equipo, on_delete=models.SET(get_sentinel_user))
    Cliente= models.ForeignKey(Cliente, on_delete=models.SET(get_sentinel_user))
    choicesEstado= (('PROCESANDO','Procesando'),('ESPERA','En espera'), ('TERMINADO','Terminado'),('ENTREGADO', 'Entregado'))
    Estado =  models.CharField(max_length = 20, choices= choicesEstado, default=choicesEstado[0][0] )
    #devuelve url con la vista, los argumentos (kwargs) # para  

    #devuelve una direccion url conformada por la el urlpatern Detalle-Ordenes con los argumentos pk del modelo 
    def get_absolute_url(self):
        return reverse('index:Detalle-Ordenes', kwargs={'pk':self.pk})

    def __str__(self):
        return 'orden '+ str(self.id)