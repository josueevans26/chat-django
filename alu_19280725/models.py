from django.db import models

# Create your models here.

class Contactos(models.Model):
    nombre = models.CharField(max_length=50)
    ap_pat = models.CharField(max_length=50)
    ap_mat = models.CharField(max_length=50)
    status = models.SmallIntegerField()

    def __str__(self):
        return '%s %s %s' % (self.nombre,self.ap_pat,self.ap_mat)
    
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'ap_pat': self.ap_pat,
            'ap_mat': self.ap_mat,
            'status': self.status,
        }

class Mensajes(models.Model):
    contenido = models.CharField(max_length=500)
    contacto = models.ForeignKey(Contactos, on_delete=models.CASCADE)
    status = models.SmallIntegerField()

    def __str__(self):
        return '%s %s %s' % (self.contacto.nombre, self.contacto.ap_pat, self.contenido)
    
    def to_dict(self):
        return {
            'id': self.id,
            'contenido': self.contenido,
            'status': self.status,
            'contacto': self.contacto.to_dict(),
        }
    
    